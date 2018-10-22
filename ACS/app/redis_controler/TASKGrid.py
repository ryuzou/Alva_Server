import redis
import os
import sys

try:
    from ..redis_controler import Init
except Exception:
    import Init

__init = None
redis_db = None


def __Init():
    global __init
    if __init != 1:
        __init_TASKGrid()
        Init.__Init()
        global redis_db
        redis_db = Init.redis_db
        __init = 1
    else:
        pass
    return 0


def __init_TASKGrid():
    __Init()
    global redis_db
    redis_db.lpush('TASKGRID', 'CMD_NONE')


def GetTASKGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lpop('TASKGRID')
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
        text = "__arg" + c + "_" + n
        Text += text
    if redis_db.lpush('TASKGRID', Text) != 0:
        return -1
    else:
        return 0
