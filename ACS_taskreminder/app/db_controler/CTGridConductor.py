try:
    from ..db_controler import Init
    from ..db_controler import COMMNADGrid
    from ..db_controler import TASKGrid
    from ..db_controler import CurrentCMDGrid
except Exception:
    import Init
    import COMMNADGrid
    import TASKGrid
    import UniqueIDGrid


class Commands():
    UniqueID = None
    priority = 0
    Taskgrid = None
    initd = 0

    def __init__(self):
        self.UniqueID = CurrentCMDGrid.UIDGrid.GETANDINSERTUID()
        self.Taskgrid = TASKGrid.TaskGrid()
        self.Taskgrid.InitGrid(self.UniqueID)
        # COMMNADGrid.InsertCOMMANDGrid_least(Uid=self.UniqueID, priority=self.priority)

    def SetHogestPriority(self):
        self.priority = 1

    def InsertCommand(self, command, *args):
        if self.initd == 0:
            COMMNADGrid.CMDGRID.InsertCOMMANDGrid_least(Uid=self.UniqueID, priority=self.priority)
            self.initd = 1
        self.Taskgrid.InsertTASKGrid_least(command, args)
