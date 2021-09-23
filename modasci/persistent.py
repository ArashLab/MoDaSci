import abc

from munch import Munch

from .path import Path
from .serialization import YAMLMixin
from .storage import Storage
from .utils import import_class as _import_class


class Persistent(Storage, YAMLMixin, abc.ABC):
    """Base class for persistent storages.

    A persistent storage must expose two *gateways*, one for reading from it, and one for writing to it. These will be
    defined in the form of two abstract property methods which must be overridden.

    Attributes
    ----------
    path: Path
        Contains details about the provided path.

    Parameters
    ----------
    plainStorage: Munch
        Description for the persistent storage.
    """

    def __init__(self, plainStorage, settings):
        self.path = Path(plainStorage.path, settings)

    @abc.abstractmethod
    def read(self):
        """
        A context manager for reading data from the file.
        """
        pass

    @abc.abstractmethod
    def write(self):
        """
        A context manager for writing data to the file.
        """
        pass

    def toDict(self):
        return {'path': self.path.raw}


def import_class(identifier):
    return _import_class('persistents', identifier)
