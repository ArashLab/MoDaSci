from ..micro_task import MicroTask

import pandas as pd
import hail as hl

class KeyBy(MicroTask):

    def execute(self, volatileData):
        if isinstance(volatileData, hl.MatrixTable):
            func = getattr(volatileData, f'key_{self.parameters.axis}s_by')
            data = func(*self.parameters.keys)
        elif isinstance(volatileData, hl.Table):
            data = volatileData.key_by(*self.parameters.keys)
        return data