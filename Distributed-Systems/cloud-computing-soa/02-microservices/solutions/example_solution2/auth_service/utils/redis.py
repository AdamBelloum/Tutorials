import redis.asyncio as async_redis
import redis
import time

class Redis:
    # Bonus (Async Redis server usage for scalability)
    @staticmethod
    def get_redis_connection(retries=3, delay=2, host='localhost'):
        """
        Function to get a async redis connection
        :param retries: Number of times to retry connection
        :param delay: Wait time between retries
        :return: Async redis connection
        """
        for _ in range(retries):
            try:
                redis_connection = async_redis.Redis(host=host, port=6379, db=0)
                return redis_connection
            except redis.exceptions.ConnectionError:
                time.sleep(delay)
        return None