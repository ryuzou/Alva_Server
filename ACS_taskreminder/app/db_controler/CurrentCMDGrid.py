try:
    from ..db_controler import Init
except Exception:
    import Init


class CCMDGRID():
    redis_db = None

    def __init__(self, REDIS=Init.REDISDB):
        self.redis_db = REDIS.redis_db
        self.__init_CCMDGrid()

    def __init_CCMDGrid(self):
        self.redis_db.set('CCMDGRID', 0)

    def UpdateCCMD(self, num):
        return self.redis_db.set('CCMDGRID', int(num))

    def GetCCMD(self):
        return int(self.redis_db.get('CCMDGRID'))


CCMD = CCMDGRID()
