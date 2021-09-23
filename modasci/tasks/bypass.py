from numpy import e
from modasci import utils
from ..task import Task

import hail as hl
import pandas as pd

class Bypass(Task):

    def execute(self):
        srcData = self.dataConnectors.source.values

        convert = self.parameters.get('convert')

        if convert == None:
            pass
        else:
            srcFormat = convert.get('form')
            destFormat = convert.get('to')

            if srcFormat == 'HailTable':
                if destFormat == 'HailTable':
                    pass
                elif destFormat == 'PandasDataFrame':
                    destData = srcData.to_pandas()
                elif destFormat == 'HailMatrixTable':
                    destData = hl.MatrixTable.from_rows_table(srcData)

            elif srcFormat == 'HailMatrixTable':
                if destFormat == 'HailMatrixTable':
                    pass
                else:
                    axis = self.parameters.get('axis')
                    if axis == 'rows':
                        destData = srcData.rows()
                    elif axis == 'cols':
                        destData = srcData.cols()

                    if destFormat == 'HailTable':
                        pass
                    elif destFormat == 'PandasDataFrame':
                        destData = srcData.to_pandas()

            if srcFormat == 'PandasDataFrame':
                if destFormat == 'PandasDataFrame':
                    pass
                elif destFormat == 'HailTable':
                    destData = hl.Table.from_pandas(srcData)
                elif destFormat == 'HailMatrixTable':
                    destData = hl.Table.from_pandas(srcData)
                    destData = hl.MatrixTable.from_rows_table(srcData)
        
        self.dataConnectors.destination.values = destData
