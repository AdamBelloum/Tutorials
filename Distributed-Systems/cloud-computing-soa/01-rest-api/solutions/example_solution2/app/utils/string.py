from pydantic import ValidationError
import re

from app.constants.const import URL_PATTERN, SHA1_REGEX
from app.utils.redis import Redis
from app.schemas.url import UrlCreate, UrlUpdate, UrlModel

class String:
    @staticmethod
    def validate_url(url):
        """
        Function to validate the url
        :param url: URL to validate
        :return: Boolean
        """
        # check length and not None
        if url is None or len(url) == 0:
            return False
        
        # check pattern
        pattern = re.compile(URL_PATTERN)
        match = pattern.fullmatch(url)
        return match is not None
    
    @staticmethod
    async def shorten_url():
        """
        Function to increment URL counter and encode it into SHA-1 hash value
        :return: 8 character SHA-1 hash value
        """
        counter_for_url = await Redis.increment_counter()
        print(f'During shortening, counter value for url: {counter_for_url}')
        id = Redis.encode_counter(counter_for_url)
        print(f'After Shortening id by encoding counter: {id}')
        return id
    
    @staticmethod
    def is_valid_sha1_hash(id: str):
        """
        Function to validate ID against SHA-1 hash value pattern and length of characters we choose
        :param id: URL encoded ID
        :return: Boolean
        """
        if id is None or len(id) == 0:
            return False
        pattern = re.compile(SHA1_REGEX, re.IGNORECASE)
        return pattern.fullmatch(id) and len(id) == 8

    @staticmethod
    def is_valid_http_url(url):
        """
        (Bonus - additional URL validation method)
        Function to validate URL against Pydantic HttpUrl model.
        Based on url instance given, it understands URL value from update/create requests,
        checks if URL strings are valid
        :param url: URL we want to validate
        :return: Boolean
        """
        if isinstance(url, UrlCreate):
            try:
                UrlModel(url=url.value)
            except ValidationError as e:
                print(e)
                return False
        elif isinstance(url, UrlUpdate):
            try:
                UrlModel(url=url.url)
            except ValidationError as e:
                print(e)
                return False
        return True
