from .dataconnector import DataConnector

class Job:

    def __init__(self, plainJob):
        self.spec = plainJob.spec
        self.parameters = plainJob.parameters
        self.dataConnectors = {name: DataConnector(plianDataConnector) for name, plianDataConnector in plainJob.dataConnectors.items()}

    def __iter__(self):
        yield 'spec', self.spec
        yield 'parameters', self.parameters
        yield 'dataConnectors', {name: dict(dataConnector) for name, dataConnector in self.dataConnectors.items()}