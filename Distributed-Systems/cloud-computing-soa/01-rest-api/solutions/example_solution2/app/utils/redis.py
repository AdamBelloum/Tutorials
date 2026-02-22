import redis
import redis.asyncio as async_redis
import time
import hashlib

from app.constants.const import URL_COUNTER

class Redis:
    # Bonus (Async Redis server usage for scalability)
    @staticmethod
    def get_redis_connection(retries=3, delay=2):
        """
        Function to get a async redis connection
        :param retries: Number of times to retry connection
        :param delay: Wait time between retries
        :return: Async redis connection
        """
        for _ in range(retries):
            try:
                redis_connection = async_redis.Redis(host='localhost', port=6379, db=0)
                return redis_connection
            except redis.exceptions.ConnectionError:
                time.sleep(delay)
        return None

    @staticmethod
    async def increment_counter():
        """
        Function to increment URL_COUNTER key on redis server
        :return: Integer counter value after increment
        """
        await Redis.get_redis_connection().incr(URL_COUNTER)
        counter_value = await Redis.get_redis_connection().get(URL_COUNTER)
        print(f"Incremented counter to reflect number of urls: {counter_value}")
        return counter_value

    @staticmethod
    async def reset_counter():
        """
        Function to reset URL_COUNTER key on redis server to zero
        :return: Integer counter value after reset
        """
        counter_value = await Redis.get_redis_connection().set(URL_COUNTER, 0)
        print(f"Reset redis URL counter to zero: {counter_value}")
        return counter_value

    @staticmethod
    def encode_counter(counter_value: int):
        """
        Function to encode counter value using Secure Hash Algorithm - 1 (SHA-1)
        :param counter_value: Integer counter value representing URL_COUNTER to encode
        :return: 8 character hexadecimal counter value encoded
        """
        return hashlib.sha1(str(counter_value).encode()).hexdigest()[:8]
