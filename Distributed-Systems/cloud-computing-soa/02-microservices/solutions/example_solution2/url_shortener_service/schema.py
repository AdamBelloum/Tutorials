from pydantic import BaseModel, HttpUrl
from typing import Optional

class UrlCreate(BaseModel):
    """
    Class to create url, based on post request params
    """
    value: str

class UrlUpdate(BaseModel):
    """
    Class to update a url, based on expected put request params
    """
    url: str

class UrlGetResponse(BaseModel):
    """
    Class to get a url, based on get request params
    """
    value: Optional[str] = None

class UrlCreateResponse(BaseModel):
    """
    Class for create url response, based on post response params
    """
    id: Optional[str] = None

class UrlUpdateResponse(BaseModel):
    """Class for update url response, based on expected update response params"""
    id: str
    value: str
    message: str = "Updated URL successfully"

class UrlGetAllResponse(BaseModel):
    """Class for response of get all urls, with expected response params keys"""
    keys: Optional[list[str]] = None

class UrlModel(BaseModel):
    """Class to initialize a url model using Pydantic"""
    url: HttpUrl
