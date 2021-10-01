from ..task import Task

class Bypass(Task):

    def execute(self):
        self.dataConnectors.destination.values = self.dataConnectors.source.values
