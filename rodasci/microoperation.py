import pandas as pd
import hail as hl

class MicroOperation:

    def __init__(self, microOperationDict):
        self.name = microOperationDict.Name
        self.parameter = microOperationDict.Parameter

    @property
    def microp(self):
        return self.__microp

    @microp.setter
    def microp(self, data):
        self.__microp = data

    def __GetMicropClass(self, data):
        pass
        # if isinstance(data, pd.DataFrame):
        #     return MicropPandas
        # elif isinstance(data, hl.Table):
        #     return MicropHailTable
        # elif isinstance(data, hl.MatrixTable):
        #     return MicropHailMatrixTable

    def Execute(self, data):
        micropClass = self.__GetMicropClass(data)
        micropFunction = getattr(micropClass, self.microp.name)
        micropFunction(data, self.microp.parameter)



