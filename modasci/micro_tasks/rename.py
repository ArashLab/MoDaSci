from ..micro_task import MicroTask

import pandas as pd
import hail as hl

class Rename(MicroTask):

    def execute(self, volatileData):
        if isinstance(volatileData, hl.MatrixTable) or isinstance(volatileData, hl.Table):
            return volatileData.rename(self.parameters.rename)
        