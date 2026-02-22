from sqlalchemy.future import select
from sqlalchemy import update

from auth_service.model import User
from auth_service.schemas.user import UserCreateResponse
from auth_service.utils.jwt import JWT
from auth_service.utils.auth import Auth

from auth_service.settings import settings

async def create_new_user(db, username, password):
    try:
        hash_password = await Auth.hash_password(password) # hash password
        db_user = User(
            username=username,
            password=hash_password
        )
        db.add(db_user) # add user to database
        await db.commit()
        await db.refresh(db_user)
        return UserCreateResponse(
            id=db_user.id,
            username=db_user.username
        )
    except Exception as e:
        print("Error - service: create new user", e)
        await db.rollback()
        return None
    
async def get_user_id(db, username, password):
    try:
        query = await db.execute(select(User).filter(User.username == username)) # find user by username
        user = query.scalar_one_or_none()
        if not user:
            return None
        is_correct_password = await Auth.verify_password(password, user.password)
        if is_correct_password is False: # verify the password
            return None
        return user.id
    except Exception as e:
        print("Error - service: authenticate", e)
        return None

async def get_user_by_id(db, id):
    try:
        query = await db.execute(select(User).filter(User.id == id)) # get user by id
        user = query.scalar_one_or_none()
        return user
    except Exception as e:
        print("Error - service: get user by id", e)
        return None

async def get_user_by_username(db, username):
    try:
        query = await db.execute(select(User).filter(User.username == username))
        user = query.scalar_one_or_none()
        return user
    except Exception as e:
        print("Error - service: get user by username", e)
        return None

async def validate_token(db, token):
    try:
        token_payload = JWT.verify_token(token=token, secret_key=settings.SECRET_KEY)
        user_id = token_payload.user
        user = await get_user_by_id(db, user_id)
        return user
    except Exception as e:
        print("Error - service: validate token", e)
        return None

async def update_user_password(db, username, old_password, new_password):
    try:
        # get user by username
        user = await get_user_by_username(db, username)
        if not user:
            return False
        # verify password
        is_correct_password = await Auth.verify_password(old_password, user.password)
        if is_correct_password is False:
            return False

        # update password
        hashed_password = await Auth.hash_password(new_password)
        update_stmt = (
            update(User)
            .where(User.username == username)
            .values(password=hashed_password)
        )
        await db.execute(update_stmt)
        await db.commit()

        return True
    except Exception as e:
        print("Error - service: update user password", e)
        return None