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
    def dataset(self):
        dataset = self.dataHandler.volatile.dataset
        for microOperation in self.microOperations:
            dataset = microOperation.Execute(dataset)
        return dataset

    @dataset.setter
    def dataset(self, dataset):
        for microOperation in self.microOperations:
            dataset = microOperation.Execute(dataset)
        self.dataHandler.volatile.dataset = dataset





