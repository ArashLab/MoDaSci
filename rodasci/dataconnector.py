from .microoperation import MicroOperation
class DataConnector:

    def __init__(self, dataConnectorDict):
        self.dataHandlerName = dataConnectorDict.DataHandler
        self.jobs = [MicroOperation(microOperationDict) for microOperationDict in dataConnectorDict.MicroOperations]
        



