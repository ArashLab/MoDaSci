from rodasci import Task
from rodasci.enums import DataTypes


class ByPass(Task):

    def execute(self):
        print('Task initiated.')
        
        inData = self.dataConnectors.inData.values

        inDataType = self.dataConnectors.inData.dataType
        outDataType = self.dataConnectors.outData.dataType
        
        if inDataType == DataTypes.HailMatrixTable:
            if outDataType == DataTypes.HailMatrixTable:
                outData = inData
            elif outDataType == DataTypes.HailTable:
                if self.parameters.axis == 'rows':
                    outData = inData.rows()
                elif self.parameters.axis == 'cols':
                    outData = inData.cols()
                elif self.parameters.axis == 'globals':
                    outData = inData.globals_table()
                elif self.parameters.axis == 'entries':
                    outData = inData.entries()
            else:
                pass # not supported exception
        elif inDataType == DataTypes.HailTable:
            if outDataType == DataTypes.HailTable:
                outData = inData
            elif outDataType == DataTypes.PandasDataFrame:
                outData = inData.to_pandas()
            elif outDataType == DataTypes.SparkDataFrame:
                outData = inData.to_spark()
            elif outDataType == DataTypes.SqlTable:
                outData = inData.to_spark() # or inData or inData.toPandas (what is used for sql interface)
        
        self.dataConnectors.outDat.values = outData
        

    def toDict(self):
        return {}
