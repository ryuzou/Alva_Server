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
        __init_TASKGrid()
        __init = 1
    else:
        pass
    return 0


def __init_TASKGrid():
    global redis_db
    redis_db.lpush('TASKGRID', 'CMD_NONE')


def GetTASKGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lrange('TASKGRID', -1, -1)[0]  # todo Zanteiteki shochiThe last one
    GridText = str(GridText.decode('utf-8'))
    d = {}
    for n in GridText.split("__"):
        d[n.split("_")[0]] = n.split("_")[1]
    return d


def PopTASKGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.rpop('TASKGRID')
    if GridText == None or GridText == None:
        return "NULL"
    GridText = str(GridText.decode('utf-8'))
    d = {}
    for n in GridText.split("__"):
        d[n.split("_")[0]] = n.split("_")[1]
    return d


def InsertTASKGrid_least(CMD, *args):
    __Init()
    global redis_db
    Text = "CMD_" + CMD
    c = 1
    for n in args:
        text = "__arg" + str(c) + "_" + str(n)
        Text += text
        c = c + 1
    redis_db.lpush('TASKGRID', str(Text))
    return 0
