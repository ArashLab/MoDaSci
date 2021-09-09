from .dataconnector import DataConnector

class Job:

    def __init__(self, plainJob):
        self.specifications = plainJob.Specifications
        self.parameters = plainJob.Parameters
        self.dataConnectors = {name: DataConnector(plianDataConnector) for name, plianDataConnector in plainJob.DataConnectors.items()}

    def __iter__(self):
        yield 'Specifications', self.specifications
        yield 'Parameters', self.parameters
        yield 'DataConnectors', {name: dict(dataConnector) for name, dataConnector in self.dataConnectors.items()}