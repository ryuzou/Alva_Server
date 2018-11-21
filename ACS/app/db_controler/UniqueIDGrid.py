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
        __init_UIDGrid()
        __init = 1
    else:
        pass
    return 0


def __init_UIDGrid():
    global redis_db
    redis_db.lpush('UIDGRID', '0')


def GetUIDGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lrange('UIDGRID', -1, -1)[0]  # todo Zanteiteki shochiThe last one
    GridText = str(GridText.decode('utf-8'))
    return GridText


def InsertUIDGrid_least(UID):
    __Init()
    global redis_db
    Text = UID
    redis_db.lpush('UIDGRID', str(Text))
    return 0


def GETANDINSERTUID():
    __Init()
    global redis_db
    UID = int(GetUIDGrid_least()) + 1
    InsertUIDGrid_least(UID=UID)
    return UID
