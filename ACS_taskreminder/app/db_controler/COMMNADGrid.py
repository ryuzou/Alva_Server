try:
    from ..db_controler import Init
except Exception:
    import Init


class COMMANDGRID():
    redis_db = None

    def __init__(self, REDIS=Init.REDISDB):
        self.redis_db = REDIS.redis_db
        self.__init_COMMANDGrid()

    def __init_COMMANDGrid(self):
        self.redis_db.lpush('COMMANDGRID', '')

    def GetCOMMANDGrid_least(self):
        GridText = self.redis_db.lrange('COMMANDGRID', -1, -1)[0]  # todo Zanteiteki shochiThe last one
        GridText = str(GridText.decode('utf-8'))
        return int(GridText.split("_")[1])

    def PopCOMMANDGrid_least(self):  # get unique id
        GridText = self.redis_db.rpop('COMMANDGRID')
        if GridText == None or GridText == None:
            return "NULL"
        GridText = str(GridText.decode('utf-8'))
        return int(GridText.split("_")[1])

    def InsertCOMMANDGrid_least(self, Uid, priority):
        Text = "UniqueID_" + str(Uid)
        if priority == 1:
            self.redis_db.rpush('COMMANDGRID', str(Text))
        self.redis_db.lpush('COMMANDGRID', str(Text))
        return 0


CMDGRID = COMMANDGRID()
