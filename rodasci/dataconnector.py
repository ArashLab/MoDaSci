from .microoperation import MicroOperation
class DataConnector:

    def __init__(self, plainDataConnector):
        self.dataHandlerName = plainDataConnector.DataHandlerName
        self.microOperations = [MicroOperation(plainMicroOperation) for plainMicroOperation in plainDataConnector.MicroOperations]

    def __iter__(self):
        yield 'DataHandlerName', self.dataHandlerName
        yield 'MicroOperations', [dict(microOperation) for microOperation in self.microOperations]




