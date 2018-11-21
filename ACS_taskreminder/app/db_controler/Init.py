import redis

__init = None
redis_db = None


def __Init():
    global __init
    if __init == None:
        global redis_db
        pool = redis.ConnectionPool(host='redis', port=6379, db=0)
        redis_db = redis.StrictRedis(connection_pool=pool)
        __init = 1
    else:
        pass
