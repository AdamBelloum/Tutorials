from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.url import *
from app.schemas.token import *
from app.schemas.user import *

from app.services.url_service import *
from app.services.user_service import *

from app.utils.db import get_db, reset_db
from app.utils.redis import Redis
from app.utils.string import String
from app.utils.security import Security


# Bonus - concurrent programming for DB, redis.
@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    async_redis_connection = Redis.get_redis_connection()
    print("Async redis connection in lifespan:", async_redis_connection)
    await FastAPILimiter.init(redis=async_redis_connection)
    print("Reset db..!")
    await reset_db()
    print("Redis reset ..!")
    await Redis.reset_counter()
    # Run app
    yield
    # Close
    await FastAPILimiter.close()

app = FastAPI(lifespan=lifespan)

### AUTH APIs ###
@app.post("/signin", status_code=200, response_model=Token)
async def signin(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": await Security.create_access_token(user.id),
        "token_type": "bearer",
    }

@app.post("/signup", status_code=200, response_model=UserCreateResponse)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    response = await create_new_user(db, email=user.email, password=user.password)
    if response is None:
        raise HTTPException(status_code=400, detail="Bad Input User Errors")
    return response

### URL APIs ###
# Bonus - Ratelimiter for added security
@app.post("/", response_model=UrlCreateResponse, status_code=201, description="Create new URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def create_url(url: UrlCreate, db: AsyncSession = Depends(get_db), current_user: int = Depends(Security.get_current_user)):
    response = await create_new_url(db, current_user, url)
    print("response", response)
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
async def get_urls(db: AsyncSession = Depends(get_db)):
    response = await get_all_urls(db)
    return response

@app.put("/{id}", response_model=UrlUpdateResponse, status_code=200, description="Update URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def update_url(id: str, url: UrlUpdate, db: AsyncSession = Depends(get_db), current_user: int = Depends(Security.get_current_user)):
    if await url_of_valid_id(db, id) is None: # validate id
        raise HTTPException(status_code=404, detail="Input ID/ short url not found in DB Error")
    if not String.validate_url(url.url): # validate new url
        raise HTTPException(status_code=400, detail="Bad Input URL Error")
    response = await update_url_by_id(db, current_user, id, url)
    if response is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response

@app.delete("/", status_code=404, description="Delete All URLs", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def delete_all(db: AsyncSession = Depends(get_db), current_user: int = Depends(Security.get_current_user)):
    await delete_urls(db, current_user)

@app.delete("/{id}", status_code=204, description="Delete URL", dependencies=[Depends(RateLimiter(times=20, seconds=1))])
async def delete_url(id: str, db: AsyncSession = Depends(get_db), current_user: int = Depends(Security.get_current_user)):
    response = await delete_by_id(db, current_user, id) # true or false
    if response is False:
        raise HTTPException(status_code=404, detail="Cannot delete the URL by ID")
    return