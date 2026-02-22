from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi_limiter.depends import RateLimiter
from fastapi_limiter import FastAPILimiter
from sqlalchemy.ext.asyncio import AsyncSession

from auth_service.schemas.token import *
from auth_service.schemas.user import *
from auth_service.service import *

from auth_service.utils.auth import Auth
from auth_service.utils.redis import Redis
from common_utils.db import get_db, create_tables_if_not_exist
from common_utils.util import get_env_variable
from common_utils.const import PROD_VAR, PROD_VAL


# Bonus - concurrent programming for DB, redis.
# Bonus - Rate limiter for auth service end points
@asynccontextmanager
async def lifespan(_: FastAPI):
    # Startup
    production_env = get_env_variable(PROD_VAR)
    redis_server = 'redis' if production_env == PROD_VAL else 'localhost'
    async_redis_connection = Redis.get_redis_connection(host=redis_server)
    await FastAPILimiter.init(redis=async_redis_connection)
    await create_tables_if_not_exist()
    # Run app
    yield
    # Close
    await FastAPILimiter.close()

# Bonus - rate limiter and swagger UI
app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"syntaxHighlight": False})


@app.post("/users", status_code=201, response_model=UserCreateResponse, dependencies=[Depends(RateLimiter(times=40, seconds=1))])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_in_db = await get_user_by_username(db, username=user.username)
    if user_in_db: # exising username in db -> duplicated
        raise HTTPException(status_code=409, detail="duplicate")
    
    response = await create_new_user(db, username=user.username, password=user.password)
    if response is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return response

@app.put("/users", status_code=200, dependencies=[Depends(RateLimiter(times=40, seconds=1))])
async def update_password(user: UserUpdate, db: AsyncSession = Depends(get_db)):
    response  = await update_user_password(db, username=user.username, old_password=user.old_password, new_password=user.new_password)
    if response is False:
        raise HTTPException(status_code=403, detail="forbidden")
    if response is None:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/users/login", status_code=200, response_model=Token, dependencies=[Depends(RateLimiter(times=40, seconds=1))])
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    user_id  = await get_user_id(db, username=user.username, password=user.password)
    if not user_id:
        raise HTTPException(status_code=403, detail="forbidden")
    access_token = await Auth.create_access_token(user_id)
    if not access_token:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return {
        "token": f"Bearer {access_token}"
    }

@app.post("/users/current", status_code=200, response_model=UserValidateResponse, dependencies=[Depends(RateLimiter(times=40, seconds=1))])
async def get_current_user(token: Token, db: AsyncSession = Depends(get_db)):
    user = await validate_token(db, token=token)
    if not user:
        raise HTTPException(status_code=403, detail="forbidden")
    return user
