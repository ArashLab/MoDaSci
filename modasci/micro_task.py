import abc
from pydoc import locate

from munch import Munch
from stringcase import snakecase, pascalcase

from .task_base import TaskBase


class MicroTask(TaskBase, abc.ABC):
    """Base class for micro-tasks.

    Subclass this class and override the `execute()` method to define a custom task and reference it in the workflow.
    """

    def __init__(self, parameters):
        self.parameters = parameters

    @abc.abstractmethod
    def execute(self, volatileData):
        pass

    @staticmethod
    def instantiate(plainMicroTask):
        stores = ('micro_tasks', 'rodasci.contrib.micro_tasks')
        spec = plainMicroTask.spec if isinstance(plainMicroTask, Munch) else plainMicroTask
        candidates = [locate(f'{store}.{snakecase(spec)}.{pascalcase(spec)}') for store in stores]
        cls = next(cls for cls in candidates if cls is not None)
        assert cls is not None, f'Could not import {spec}'
        # noinspection PyCallingNonCallable
        return cls(parameters=plainMicroTask.get('parameters') if isinstance(plainMicroTask, Munch) else {})
