import redis
import Init

__init = None
redis_db = None


def __Init():
    Init.__Init()
    global redis_db
    redis_db = Init.redis_db
