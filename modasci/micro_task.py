import abc

from .task_base import TaskBase
from .utils import import_class as _import_class


class MicroTask(TaskBase, abc.ABC):
    """Base class for micro-tasks.

    Subclass this class and override the `execute()` method to define a custom task and reference it in the workflow.
    """

    def __init__(self, plainMicroTask):
        self.parameters = plainMicroTask.parameters

    @abc.abstractmethod
    def execute(self, volatileData):
        pass

    def toDict(self):
        return {
            'spec': self.__class__.__name__,
            'parameters': self.parameters,
        }


def import_task(identifier):
    return _import_class('micro_tasks', identifier)
