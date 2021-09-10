from .microoperation import MicroOperation
class DataConnector:

    def __init__(self, plainDataConnector):
        self.dataHandlerName = plainDataConnector.dataHandlerName
        self.microOperations = [MicroOperation(plainMicroOperation) for plainMicroOperation in plainDataConnector.microOperations]

    def __iter__(self):
        yield 'dataHandlerName', self.dataHandlerName
        yield 'microOperations', [dict(microOperation) for microOperation in self.microOperations]




