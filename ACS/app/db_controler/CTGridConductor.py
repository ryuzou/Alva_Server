import redis
import os
import sys

try:
    from ..db_controler import Init
    from ..db_controler import COMMNADGrid
    from ..db_controler import TASKGrid
    from ..db_controler import UniqueIDGrid
except Exception:
    import Init
    import COMMNADGrid
    import TASKGrid
    import UniqueIDGrid


class Commands():
    UniqueID = None
    priority = 0
    Taskgrid = None

    def __init__(self):
        self.UniqueID = UniqueIDGrid.GETANDINSERTUID()
        self.Taskgrid = TASKGrid.TaskGrid()
        self.Taskgrid.InitGrid(self.UniqueID)
        # COMMNADGrid.InsertCOMMANDGrid_least(Uid=self.UniqueID, priority=self.priority)

    def SetHogestPriority(self):
        self.priority = 1

    def InsertCommand(self, command, *args):
        COMMNADGrid.InsertCOMMANDGrid_least(Uid=self.UniqueID, priority=self.priority)
        self.Taskgrid.InsertTASKGrid_least(command, args)
