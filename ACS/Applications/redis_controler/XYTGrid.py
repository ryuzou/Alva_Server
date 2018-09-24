import flask
import redis
import Init

__init = None
redis_db = None

def __Init():
    global __init
    if __init != 1:
        __init_XYTGrid()
        Init.__Init()
        global redis_db
        redis_db = Init.redis_db
        __init = 1
    else:
        pass
    return 0

def __init_XYTGrid():
    __Init()
    global redis_db
    redis_db.lpush('XYTGRID', 'X_0__Y_0__T_0')


def GetXYTGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lpop('XYTGRID')
    d = {}
    for n in GridText.split("__"):
        d[n.split("_")[0]] = n.split("_")[1]
    return d


def InsertXYTGrid_least(X, Y, T):
    __Init()
    global redis_db
    Text = "X_" + X + "__Y_" + Y + "__T_" + T
    if redis_db.lpush('XYTGRID', Text) != 0:
        return -1
    else:
        return 0
