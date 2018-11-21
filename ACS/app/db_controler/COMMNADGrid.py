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
        __init_COMMANDGrid()
        __init = 1
    else:
        pass
    return 0


def __init_COMMANDGrid():
    global redis_db
    redis_db.lpush('COMMANDGRID', '')


def GetCOMMANDGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lrange('COMMANDGRID', -1, -1)[0]  # todo Zanteiteki shochiThe last one
    GridText = str(GridText.decode('utf-8'))
    return GridText.split("_")[1]


def PopCOMMANDGrid_least():  # get unique id
    __Init()
    global redis_db
    GridText = redis_db.rpop('COMMANDGRID')
    if GridText == None or GridText == None:
        return "NULL"
    GridText = str(GridText.decode('utf-8'))
    return GridText.split("_")[1]


def InsertCOMMANDGrid_least(Uid, priority):
    __Init()
    global redis_db
    Text = "UniqueID_" + Uid
    if priority == 1:
        redis_db.rpush('COMMANDGRID', str(Text))
    redis_db.lpush('COMMANDGRID', str(Text))
    return 0
