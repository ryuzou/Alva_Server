import flask
import redis
import os
import sys

try:
    from ..db_controler import Init
except Exception:
    import Init


class XYTGRID():
    redis_db = None

    def __init__(self, REDIS=Init.REDISDB):
        self.redis_db = REDIS.redis_db
        self.__init_XYTGrid()

    def __init_XYTGrid(self):
        self.redis_db.lpush('XYTGRID', 'X_0__Y_0__T_0')

    def GetXYTGrid_least(self):
        GridText = self.redis_db.lrange('XYTGRID', -1, -1)[0]  # The last one
        if type(GridText) != int:
            GridText = str(GridText.decode('utf-8'))
        d = {}
        for n in GridText.split("__"):
            d[n.split("_")[0]] = n.split("_")[1]
        return d

    def InsertXYTGrid_least(self, X, Y, T):
        Text = "X_" + str(X) + "__Y_" + str(Y) + "__T_" + str(T)
        if self.redis_db.lpush('XYTGRID', Text) != 0:
            return -1
        else:
            return 0


XYTGrid = XYTGRID()
