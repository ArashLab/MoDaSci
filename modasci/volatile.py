import abc

from munch import Munch

from .serialization import YAMLMixin
from .storage import Storage
from .utils import import_class as _import_class


class Volatile(Storage, YAMLMixin, abc.ABC):
    """Base class for volatile storages.

    A volatile storage must work in conjunction with the corresponding persistent storage, capable of performing reading
    and writing operations.

    Parameters
    ----------
    plainStorage: Munch
        Description for the volatile storage.
    """

    def __init__(self, plainStorage, settings):
        self.values, self.ready = None, False
        self.importParameters = plainStorage.get('importParameters', Munch()) if plainStorage else Munch()
        self.exportParameters = plainStorage.get('exportParameters', Munch()) if plainStorage else Munch()

    @abc.abstractmethod
    def populate(self, persistent):
        pass

    @abc.abstractmethod
    def mutate(self, persistent, newValue):
        pass

    def toDict(self):
        return {
            'spec': self.__class__.__name__,
            'importParameters': self.importParameters,
            'exportParameters': self.exportParameters,
        }


def import_class(identifier):
    return _import_class('volatiles', identifier)
