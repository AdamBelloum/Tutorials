from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi_limiter.depends import RateLimiter
from fastapi_limiter import FastAPILimiter

from sqlalchemy.ext.asyncio import AsyncSession

from url_shortener_service.schema import *
from url_shortener_service.service import *

from common_utils.db import get_db, create_tables_if_not_exist
from common_utils.util import get_auth_service_host
from url_shortener_service.utils.redis import Redis
from url_shortener_service.utils.url_process import UrlProcess

import requests

AUTH_SERVICE_HOST = get_auth_service_host()

# Bonus - concurrent programming for DB, redis.
@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    async_redis_connection = Redis.get_redis_connection()
    print("Async redis connection in lifespan:", async_redis_connection)
    await FastAPILimiter.init(redis=async_redis_connection)
    await create_tables_if_not_exist()
    # Run app
    yield
    # Close
    await FastAPILimiter.close()

app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"syntaxHighlight": False})

def reusable_oauth2(request: Request):
    token = request.headers.get("Authorization")
    return token

@app.post("/", response_model=UrlCreateResponse, status_code=201, description="Create new URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def create_url(url: UrlCreate, db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)):
    auth_response = requests.post(f"{AUTH_SERVICE_HOST}/users/current", json={"token": token})
    current_user = auth_response.json()
    if auth_response.status_code != 200:
        raise HTTPException(status_code=403, detail="forbidden")
    response = await create_new_url(db, current_user["id"], url)
    if response is None:
        raise HTTPException(status_code=400, detail="error")
    return response

@app.get("/{id}", response_model=UrlGetResponse, status_code=301, description="Get URL by ID", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def get_url(id: str, db: AsyncSession = Depends(get_db)):
    response = await get_url_by_id(db, id)
    if response is None:
        raise HTTPException(status_code=404)
    return response

@app.get("/", response_model=UrlGetAllResponse, status_code=200, description="Get all URLs", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def get_urls(db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)):
    auth_response = requests.post(f"{AUTH_SERVICE_HOST}/users/current", json={"token": token})
    current_user = auth_response.json()
    if auth_response.status_code != 200:
        raise HTTPException(status_code=403, detail="forbidden")
    response = await get_all_urls(db, current_user["id"])
    return response

@app.put("/{id}", response_model=UrlUpdateResponse, status_code=200, description="Update URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def update_url(id: str, url: UrlUpdate, db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)):
    if await url_of_valid_id(db, id) is None: # validate id
        raise HTTPException(status_code=404, detail="Input ID/ short url not found in DB Error")
    if not UrlProcess.validate_url(url.url): # validate new url
        raise HTTPException(status_code=400, detail="Bad Input URL Error")

    auth_response = requests.post(f"{AUTH_SERVICE_HOST}/users/current", json={ "token": token })
    current_user = auth_response.json()
    if auth_response.status_code != 200:
        raise HTTPException(status_code=403, detail="forbidden")
    response = await update_url_by_id(db, current_user["id"], id, url)
    if response is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response

@app.delete("/", status_code=404, description="Delete All URLs", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def delete_all(db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)):
    auth_response = requests.post(f"{AUTH_SERVICE_HOST}/users/current", json={"token": token})
    current_user = auth_response.json()
    if auth_response.status_code != 200:
        raise HTTPException(status_code=403, detail="forbidden")
    await delete_urls(db, current_user["id"])

@app.delete("/{id}", status_code=204, description="Delete URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def delete_url(id: str, db: AsyncSession = Depends(get_db), token: str = Depends(reusable_oauth2)):
    auth_response = requests.post(f"{AUTH_SERVICE_HOST}/users/current", json={"token": token})
    current_user = auth_response.json()
    if auth_response.status_code != 200:
        raise HTTPException(status_code=403, detail="forbidden")
    response = await delete_by_id(db, current_user["id"], id) # true or false
    if response is False:
        raise HTTPException(status_code=404, detail="Cannot delete the URL by ID")
    return
