import flask
import redis
import Init

__init = None
redis_db = None

def __Init():
    Init.__Init()
    global redis_db
    redis_db = Init.redis_db

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


def InsertXYTGrid_least(X, Y, T):
    __Init()
    global redis_db
    Text = "__X_" + X + "__Y_" + Y + "__T_" + T
    if redis_db.lpush('XYTGRID', Text) != 0:
        return -1
    else:
        return 0
