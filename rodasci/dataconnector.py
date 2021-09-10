from .microoperation import MicroOperation
class DataConnector:

    def __init__(self, plainDataConnector):
        self.dataHandlerName = plainDataConnector.dataHandlerName
        self.microOperations = [MicroOperation(plainMicroOperation) for plainMicroOperation in plainDataConnector.microOperations]

    def __iter__(self):
        yield 'dataHandlerName', self.dataHandlerName
        yield 'microOperations', [dict(microOperation) for microOperation in self.microOperations]

    def SetDataHanlder(self, dataHandlers):
        self.dataHandler = dataHandlers[self.dataHandlerName]

    @property
    def volatileData(self):
        volatileData = self.dataHandler.volatile.data
        for microOperation in self.microOperations:
            volatileData = microOperation.Execute(volatileData)
        return volatileData

    @volatileData.setter
    def volatileData(self, volatileData):
        for microOperation in self.microOperations:
            volatileData = microOperation.Execute(volatileData)
        self.dataHandler.volatile.data = volatileData





