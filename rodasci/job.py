from .dataconnector import DataConnector

class Job:

    def __init__(self, jobDict):
        self.specifications = jobDict.Specifications
        self.parameters = jobDict.Parameters
        self.dataConnectors = {name: DataConnector(dataConnectorDict) for name, dataConnectorDict in jobDict.DataConnectors.items()}
