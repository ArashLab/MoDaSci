from ..micro_task import MicroTask

import pandas as pd
import hail as hl

class Sample(MicroTask):
    """Subsample a dataframe by number of items or fraction of items to be selected

    Subsample a dataframe by number of items `n` or fraction of items `f` to be selected.
    The `axis` parameter is needed for Hail MatrixTable.
    If `n` is provided then `f` is ignored.
    Subsampling Hail Table and MatrixTable by number of items is approximate. Since Hail only provide subsampling by fraction, we first count number of items and identify the fraction to be subsampled. The result of subsampled data may not contain exact number of items.
    """

    def execute(self, volatileData):
        if isinstance(volatileData, hl.MatrixTable) or isinstance(volatileData, hl.Table):
            n = self.parameters.get('n', None)
            f = self.parameters.get('f', None)
            axis = self.parameters.get('axis', None)
            if f:
                p = f
            elif n:
                if isinstance(volatileData, hl.MatrixTable):
                    if axis == 'row':
                        cnt = volatileData.count_rows()
                    elif axis == 'col':
                        cnt = volatileData.count_cols()
                elif isinstance(volatileData, hl.Table):
                    cnt = volatileData.count()
                p = n / cnt
            if p >= 1:
                result = volatileData
            else:
                if isinstance(volatileData, hl.MatrixTable):
                    if axis == 'row':
                        result = volatileData.sample_rows(p)
                    elif axis == 'col':
                        result = volatileData.sample_cols(p)
                elif isinstance(volatileData, hl.Table):
                    result = volatileData.sample(p)
        return result
        