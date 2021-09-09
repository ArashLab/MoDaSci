import pandas as pd
import hail as hl

from .microp import *

class MicroOperation:

    def __init__(self, plainMicroOperation):
        self.name = plainMicroOperation.Name
        self.parameter = plainMicroOperation.Parameter
        
    def __iter__(self):
        yield 'Name', self.name
        yield 'Parameters', self.parameters

    @property
    def microp(self):
        return self.__microp

    @microp.setter
    def microp(self, data):
        self.__microp = data

    def __GetMicropClass(self, data):
        pass
        if isinstance(data, pd.DataFrame):
            return MicropPandas
        elif isinstance(data, hl.Table):
            return MicropHailTable
        elif isinstance(data, hl.MatrixTable):
            return MicropHailMatrixTable

    def Execute(self, data):
        micropClass = self.__GetMicropClass(data)
        micropFunction = getattr(micropClass, self.microp.name)
        micropFunction(data, self.microp.parameter)



