from sqlalchemy.future import select
from sqlalchemy import delete, update

from app.utils.string import String
from app.models.url import URL
from app.schemas.url import UrlCreateResponse, UrlGetResponse, UrlUpdateResponse, UrlGetAllResponse


async def get_url_by_id(db, id):
    """
    Get url by ID
    :param db: Async DB session
    :param id: 8 character url id
    :return: UrlGetResponse object with url details
    """
    try:
        # check if url is valid
        url = await url_of_valid_id(db, id)
        if url is None:
            return None
        # if valid, return url
        return UrlGetResponse(value=url.value)
    except Exception as e:
        print("Error - service: get url by id", e)
        return None

async def get_all_urls(db):
    """
    Function to get all existing urls from database
    :param db: Async DB session
    :return: UrlGetAllResponse object with all urls as keys
    """
    try:
        # get all urls in DB
        result = await db.execute(select(URL))
        url_objects = result.scalars().all()
        if not url_objects: # not found
            return UrlGetAllResponse(keys=[])
        url_keys = [url_object.id for url_object in url_objects] # only get ids of URLs
        return UrlGetAllResponse(keys=url_keys)
    except Exception as e:
        print("Error - service: get urls", e)
        return UrlGetAllResponse(keys=[])

async def create_new_url(db, user_id, url):
    """
    Function to create new url
    :param db: Async DB session
    :param user_id: Integer id of user
    :param url: URL to be added to the DB
    :return: UrlCreateResponse object with url details
    """
    try:
        if String.validate_url(url.value) is False: # validate the url
            return None
        id = await String.shorten_url()

        while await get_url_by_id(db, id) is not None: # exist id
            id = await String.shorten_url() # shorten the url
        db_url = URL(
            id=id,
            value=url.value,
            user_id=user_id # bonus: url will have a owner
        )
        db.add(db_url) # create a new url in db
        await db.commit()
        await db.refresh(db_url)
        return UrlCreateResponse(id=id)
    except Exception as e:
        print("Error - service: create new url", e)
        await db.rollback()
        return None

async def url_of_valid_id(db, id):
    """
    Function to check if ID is valid, then get corresponding url from database.
    If ID is not valid, return None
    :param db: Async DB session
    :param id: 8 charecter SHA-1 encoded ID
    :return: URL string if valid, else None
    """
    # Returns valid url from db, if id is valid, else None
    if not String.is_valid_sha1_hash(id): # check id format
        return None
    result = await db.execute(select(URL).filter(URL.id == id)) # find the url by id
    return result.scalar_one_or_none()

async def update_url_by_id(db, user_id, id, url):
    """
    Function to update existing url from database.
    :param db: Async DB session
    :param user_id: Integer identifier of the user
    :param id: 8 charecter SHA-1 encoded ID
    :param url: URL string to update
    :return: UrlUpdateResponse object with updated url, id and success message
    """
    try:
        # find the url by id (bonus: user can only update their urls)
        result = await db.execute(select(URL).filter(URL.id == id, (URL.user_id == None) | (URL.user_id == user_id)))
        old_url = result.scalar_one_or_none()
        if old_url is None:
            return None
        print(f"Before Update: {old_url.value}")

        update_stmt = (
            update(URL)
            .where(URL.id == id, (URL.user_id == None) | (URL.user_id == user_id)) # bonus: user can only update their urls
            .values(value=url.url)
        )
        await db.execute(update_stmt)
        await db.commit()

        # check updated result
        result = await db.execute(select(URL).filter(URL.id == id, (URL.user_id == None) | (URL.user_id == user_id)))
        updated_url = result.scalar_one_or_none()
        print(f"After Update: {updated_url.value}")
        return UrlUpdateResponse(id=old_url.id, value=old_url.value)
    except Exception as e:
        print("Error - service: update url by id", e)
        await db.rollback()
        return None

async def delete_by_id(db, user_id, id):
    """
    Function to delete existing url from database.
    :param db: Async DB session
    :param user_id: Integer id of the user
    :param id: 8 charecter SHA-1 encoded ID
    :return: Boolean representing success
    """
    try:
        # get URL by id (bonus: user can only delete URLs they own)
        result = await db.execute(select(URL).filter(URL.id == id, (URL.user_id == None) | (URL.user_id == user_id)))
        url = result.scalar_one_or_none()
        if url is None:
            return False # fail: cannot delete

        # delete it
        await db.delete(url)
        await db.commit()
        
        return True # can delete
    except Exception as e:
        print("Error - service: delete url by id", e)
        await db.rollback()
        return False

async def delete_urls(db, user_id):
    """
    Function to delete all existing urls from database.
    :param db: Async DB session
    :param user_id: Integer id of the user
    :return:
    """
    try:
        # delete all URLs (bonus: user can only delete URLs they own)
        await db.execute(delete(URL).filter((URL.user_id == user_id) |  (URL.user_id == None)))
        await db.commit()
    except Exception as e:
        print("Error - service: delete all urls", e)
        await db.rollback()
