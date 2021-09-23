import abc


class Storage(abc.ABC):
    """Base class to all storages.

    The `Storage` is subclassed by both `Persistent` and `Volatile`, allowing for the definition of an interface for
    their common methods and attributes.
    """

    @property
    def name(self):
        return self.__class__.__name__
