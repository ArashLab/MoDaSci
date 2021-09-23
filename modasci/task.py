import abc

from munch import Munch

from .data_connector import DataConnector
from .task_base import TaskBase
from .utils import import_class as _import_class


class Task(TaskBase, abc.ABC):
    """Base class for normal tasks.

    Subclass this class and override the `execute()` method to define a custom task and reference it in the workflow.
    """

    def __init__(self, plainTask, dataHandlers):
        self.parameters = plainTask.get('parameters', Munch({}))
        self.dataConnectors = Munch({label: DataConnector(plainDataConnector, dataHandlers[plainDataConnector.dataHandler])
                                     for label, plainDataConnector in plainTask.dataConnectors.items()})

    @abc.abstractmethod
    def execute(self):
        pass

    def toDict(self):
        return {
            'spec': self.__class__.__name__,
            'parameters': self.parameters,
            'dataConnectors': self.dataConnectors,
        }


def import_class(identifier):
    return _import_class('tasks', identifier)
