from .datahandler import DataHandler
from .job import Job

class Workflow:

    def __init__(self, workflowDict):
        self.dataHandlers = {name: DataHandler(dataHandlerDict) for name, dataHandlerDict in workflowDict.DataHandlers.items()}
        self.jobs = {name: Job(jobDict) for name, jobDict in workflowDict.Jobs.items()}




