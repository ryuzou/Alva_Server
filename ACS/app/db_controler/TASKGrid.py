import redis
import os
import sys

# todo HAD MANY CHANGES IN THE MAIN SYSTEM!!!
try:
    from ..db_controler import Init as DBINIT
except Exception:
    import Init as DBINIT

class TaskGrid():
    redis_db = None
    UniqueID = None

    def __init__(self, REDIS=DBINIT.REDISDB):
        self.redis_db = REDIS.redis_db

    def InitGrid(self, UID):
        self.UniqueID = str(UID)
        self.redis_db.lpush(self.UniqueID, 'CMD_NONE')

    def GetGrid_least(self):
        GridText = self.redis_db.lrange(self.UniqueID, -1, -1)[0]
        GridText = str(GridText.decode('utf-8'))
        d = {}
        for n in GridText.split("__"):
            d[n.split("_")[0]] = n.split("_")[1]
        return d

    def PopTASKGrid_least(self):
        GridText = self.redis_db.rpop(self.UniqueID)
        if GridText == None:
            return "NULL"
        GridText = str(GridText.decode('utf-8'))
        d = {}
        for n in GridText.split("__"):
            d[n.split("_")[0]] = n.split("_")[1]
        return d

    def InsertTASKGrid_least(self, CMD, *args):
        Text = "CMD_" + CMD
        c = 1
        for n in args:
            text = "__arg" + str(c) + "_" + str(n)
            Text += text
            c = c + 1
        self.redis_db.lpush(self.UniqueID, str(Text))
        return 0
