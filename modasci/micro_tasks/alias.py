from ..micro_task import MicroTask

import pandas as pd
import hail as hl

class Alias(MicroTask):

    def execute(self, volatileData):
        if isinstance(volatileData, hl.MatrixTable) or isinstance(volatileData, hl.Table):
            colName= self.parameters.colName
            mapper = hl.dict(self.parameters.mapper)
            expr = {colName: hl.rbind(volatileData[colName], lambda value: mapper[value])}
            return volatileData.annotate(**expr)
        