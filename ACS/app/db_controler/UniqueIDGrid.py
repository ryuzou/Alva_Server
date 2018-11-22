import redis
import os
import sys

try:
    from ..db_controler import Init
except Exception:
    import Init


class UIDGRID():
    redis_db = None

    def __init__(self, REDIS=Init.REDISDB):
        self.redis_db = REDIS.redis_db
        self.__init_UIDGrid()

    def __init_UIDGrid(self):
        self.redis_db.lpush('UIDGRID', '0')

    def GetUIDGrid_First(self):
        GridText = self.redis_db.lrange('UIDGRID', 0, 0)[0]  # todo Zanteiteki shochiThe last one
        GridText = str(GridText.decode('utf-8'))
        return GridText

    def InsertUIDGrid_First(self, UID):
        Text = UID
        self.redis_db.lpush('UIDGRID', str(Text))
        return 0

    def GETANDINSERTUID(self):
        UID = int(self.GetUIDGrid_First()) + 1
        self.InsertUIDGrid_First(UID)
        return UID


UIDGrid = UIDGRID()
