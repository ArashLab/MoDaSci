import abc
from pydoc import locate

from munch import Munch
from stringcase import snakecase, pascalcase

from .data_connector import DataConnector
from .task_base import TaskBase


class Task(TaskBase, abc.ABC):
    """Base class for normal tasks.

    Subclass this class and override the `execute()` method to define a custom task and reference it in the workflow.
    """

    def __init__(self, parameters, dataConnectors):
        self.parameters = parameters
        self.dataConnectors = dataConnectors

    @abc.abstractmethod
    def execute(self):
        pass

    @staticmethod
    def instantiate(plainTask, dataHandlers):
        stores = ('tasks', 'rodasci.contrib.tasks')
        spec = plainTask.spec if isinstance(plainTask, Munch) else plainTask
        candidates = [locate(f'{store}.{snakecase(spec)}.{pascalcase(spec)}') for store in stores]
        cls = next(cls for cls in candidates if cls is not None)
        assert cls is not None, f'Could not import {spec}'
        dataConnectors = {}
        for identifier, plainDataConnector in plainTask.get('dataConnectors', {}).items():
            dataHandler = plainDataConnector.dataHandler if isinstance(plainDataConnector, Munch) else plainDataConnector
            microTasks = plainDataConnector.get('microTasks', {}) if isinstance(plainDataConnector, Munch) else {}
            plainDataConnector = {'dataHandler': dataHandler, 'microTasks': microTasks}
            dataConnectors[identifier] = DataConnector(plainDataConnector, dataHandlers[dataHandler])
        # noinspection PyCallingNonCallable
        return cls(parameters=plainTask.get('parameters'), dataConnectors=Munch(dataConnectors))
