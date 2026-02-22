import re

from url_shortener_service.utils.redis import Redis

URL_PATTERN = r"([a-zA-Z]+:\/\/)?([\w-]+\.)+([\w]{2,6})(\/.*)?"
SHA1_REGEX = r'^[0-9a-f]{8}$'

class UrlProcess:
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