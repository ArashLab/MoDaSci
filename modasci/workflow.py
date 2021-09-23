import os
from typing import Dict, List

from dacite import from_dict
from munch import Munch

from .data_handler import DataHandler
from .serialization import YAMLMixin
from .settings import Settings
from .task import import_class


class Workflow(YAMLMixin):
    """Represents a workflow.

    The class represents a workflow configured based on the passed `plainWorkflow`, which is typically loaded from
    a YAML description file.

    Attributes
    ----------
    dataHandlers: Dict[str, DataHandler]
        Contains all the data handlers defined in the workflow.
    tasks: List[TaskBase]
        Contains all the jobs defined in the workflow, in the same order that they are defined.

    Parameters
    ----------
    plainWorkflow: Munch
        The description of the workflow.
    """

    def __init__(self, plainWorkflow):
        self.settings = from_dict(Settings, plainWorkflow.get('config', {}).get('settings', {}))
        self.injectEnvVars(plainWorkflow.get('config', {}).get('environ', {}))
        self.dataHandlers = {identifier: DataHandler(plainDataHandler, self.settings)
                             for identifier, plainDataHandler in plainWorkflow.dataHandlers.items()}
        self.tasks = [import_class(plainTask.spec)(plainTask, self.dataHandlers) for plainTask in plainWorkflow.tasks]

    def injectEnvVars(self, di):
        for key, value in di.items():
            if key not in os.environ or self.settings.overrideEnvVar:
                os.environ[key] = value

    def start(self):
        """
        Executes the tasks of the workflow in the same order that they are defined.
        """
        for task in self.tasks:
            task.execute()

    def toDict(self):
        return {
            'dataHandlers': {identifier: dataHandler.toDict() for identifier, dataHandler in self.dataHandlers.items()},
            'tasks': [task.toDict() for task in self.tasks]
        }
