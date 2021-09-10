from .datahandler import DataHandler
from .job import Job

class Workflow:

    def __init__(self, plainWorkflow):
        self.dataHandlers = {name: DataHandler(plainDataHandler) for name, plainDataHandler in plainWorkflow.dataHandlers.items()}
        self.jobs = {name: Job(plainJob) for name, plainJob in plainWorkflow.jobs.items()}

        ### Set dataHandler for all jobs' dataConnectors
        for job in self.jobs.values():
            for dataConnector in job.dataConnectors.values():
                dataConnector.SetDataHanlder(self.dataHandlers)

    def __iter__(self):
        yield 'dataHandlers', {name: dict(dataHandler) for name, dataHandler in self.dataHandlers.items()}
        yield 'jobs', {name: dict(job) for name, job in self.jobs.items()}




