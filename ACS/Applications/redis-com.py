import flask
import redis

__init = None
redis_db = None


def __Init():
    global __init
    if __init == None:
        global redis_db
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        redis_db = redis.StrictRedis(connection_pool=pool)
        __init = 1
        __init_XYTGrid()
    else:
        pass


def __init_XYTGrid():
    __Init()
    global redis_db
    redis_db.lpush('XYTGRID', '__X_0__Y_0__T_0')


def GetXYTGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lpop('XYTGRID')
    X = GridText.split("__")[0].split("_")[1]
    Y = GridText.split("__")[1].split("_")[1]
    T = GridText.split("__")[2].split("_")[1]
    return X, Y, T
