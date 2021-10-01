from ..micro_task import MicroTask

import pandas as pd
import hail as hl

class Convert(MicroTask):

    def execute(self, volatileData):
        # TODO: Implement Short DataType Name (To be submitted as issue)
        srcFormat = self.parameters.get('from')
        destFormat = self.parameters.get('to')

        if srcFormat == destFormat:
            return volatileData

        if srcFormat == 'HailTable':
            if destFormat == 'PandasDataFrame':
                return volatileData.to_pandas()
            elif destFormat == 'HailMatrixTable':
                return hl.MatrixTable.from_rows_table(volatileData)
            elif destFormat == 'SparkDataFrame':
                return volatileData.to_spark()

        elif srcFormat == 'HailMatrixTable':
            axis = self.parameters.axis
            if axis == 'row':
                ht = volatileData.rows()
            elif axis == 'col':
                ht = volatileData.cols()

            if destFormat == 'HailTable':
                return ht
            elif destFormat == 'PandasDataFrame':
                return ht.to_pandas()
            elif destFormat == 'SparkDataFrame':
                return ht.to_spark()

        if srcFormat == 'PandasDataFrame':
            if destFormat == 'HailTable':
                return hl.Table.from_pandas(volatileData)
            elif destFormat == 'HailMatrixTable':
                ht = hl.Table.from_pandas(volatileData)
                return hl.MatrixTable.from_rows_table(ht)
            elif destFormat == 'SparkDataFrame':
                # TODO:
                assert False, 'Not Supported yet'

    # TODO: use the following style in the future  (To be submitted as issue)

    # # Don't import any dependencies in the global scope. Import only in their corresponding methods.
    # def execute(self, volatileData):
    #     conversions = {
    #         ('HailMatrixTable', 'HailTable'      ): self.HailMatrixTable_To_HailTable,
    #         ('HailMatrixTable', 'PandasDataFrame'): self.HailMatrixTable_To_PandasDataFrame,
    #         ('HailTable'      , 'HailMatrixTable'): self.HailTable_To_HailMatrixTable,
    #         ('HailTable'      , 'PandasDataFrame'): self.HailTable_To_PandasDataFrame,
    #         ('PandasDataFrame', 'HailTable'      ): self.PandasDataFrame_To_HailTable,
    #         ('PandasDataFrame', 'HailMatrixTable'): self.PandasDataFrame_To_HailTable,
    #         # The rest will follow here.
    #     }
    #     convert_func = conversions[(self.parameters.get('from'), self.parameters.get('to'))]
    #     return convert_func(volatileData)

    # @staticmethod
    # def dataframe_to_table(dataframe):
    #     try:
    #         import pandas as pd
    #         import hail as hl
    #     except ImportError:
    #         print('better raise an appropriate exception')  # ToDo
    #     else:
    #         return hl.Table.from_pandas(dataframe)

    # @staticmethod
    # def table_to_dataframe(hailTable):
    #     try:
    #         import pandas as pd
    #         import hail as hl
    #     except ImportError:
    #         print('better raise an appropriate exception')  # ToDo
    #     else:
    #         return some_func_idk_the_name_of(hailTable)
