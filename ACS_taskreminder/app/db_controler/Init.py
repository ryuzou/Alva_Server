import redis


class Redis():
    __init = None
    redis_db = None

    def __init__(self):
        print("initd REDIS")
        pool = redis.ConnectionPool(host='redis', port=6379, db=0)
        self.redis_db = redis.StrictRedis(connection_pool=pool)


REDISDB = Redis()
