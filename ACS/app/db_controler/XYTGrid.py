import flask
import redis
import os
import sys

try:
    from ..db_controler import Init
except Exception:
    import Init

__init = None
redis_db = None

def __Init():
    global __init
    if __init != 1:
        Init.__Init()
        global redis_db
        redis_db = Init.redis_db
        __init_XYTGrid()
        __init = 1
    else:
        pass
    return 0

def __init_XYTGrid():
    global redis_db
    redis_db.lpush('XYTGRID', 'X_0__Y_0__T_0')


def GetXYTGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lrange('XYTGRID', 0, 0)
    GridText = str(GridText[0].decode('utf-8'))
    d = {}
    for n in GridText.split("__"):
        d[n.split("_")[0]] = n.split("_")[1]
    return d


def InsertXYTGrid_least(X, Y, T):
    __Init()
    global redis_db
    Text = "X_" + str(X) + "__Y_" + str(Y) + "__T_" + str(T)
    if redis_db.lpush('XYTGRID', Text) != 0:
        return -1
    else:
        return 0
