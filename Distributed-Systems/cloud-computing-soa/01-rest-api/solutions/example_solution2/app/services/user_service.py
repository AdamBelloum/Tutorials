from sqlalchemy.future import select

from app.models.user import User
from app.schemas.user import UserCreateResponse

from app.utils.security import Security

async def create_new_user(db, email, password):
    try:
        hash_password = await Security.hash_password(password) # hash password
        db_user = User(
            email=email,
            password=hash_password
        )
        db.add(db_user) # add user to database
        await db.commit()
        await db.refresh(db_user)
        return UserCreateResponse(
            id=db_user.id,
            email=db_user.email
        )
    except Exception as e:
        print("Error - service: create new user", e)
        await db.rollback()
        return None
    
async def authenticate(db, email, password):
    try:
        query = await db.execute(select(User).filter(User.email == email)) # find user by email
        user = query.scalar_one_or_none()
        if not user:
            return None
        if not await Security.verify_password(password, user.password): # verify the password
            return None
        return user
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