from ..task import Task


class Copy(Task):

    def execute(self):
        inputs = self.dataConnectors.source.values
        self.dataConnectors.destination.values = inputs
