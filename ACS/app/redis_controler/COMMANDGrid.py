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
        __init_COMMANDGrid()
        Init.__Init()
        global redis_db
        redis_db = Init.redis_db
        __init = 1
    else:
        pass
    return 0


def __init_COMMANDGrid():
    __Init()
    global redis_db
    redis_db.lpush('COMMANDGRID', 'COMMAND_NONE')


def GetCOMMANDGrid_least():
    __Init()
    global redis_db
    GridText = redis_db.lpop('COMMANDGRID')
    d = {}
    for n in GridText.split("__"):
        d[n.split("_")[0]] = n.split("_")[1]
    return d


def InsertCOMMANDGrid_least(COMMAND, *args):
    __Init()
    global redis_db
    Text = "COMMAND_" + COMMAND
    c = 1
    for n in args:
        text = "__arg" + c + "_" + n
        Text += text
    if redis_db.lpush('COMMANDGRID', Text) != 0:
        return -1
    else:
        return 0
