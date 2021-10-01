from munch import Munch
from munch import munchify

from . import persistent, volatile
from .serialization import YAMLMixin


class DataHandler(YAMLMixin):

    @staticmethod
    def inferAttributes(plainDataHandler):
        # ToDo: Will be implemented once all attributes are settled.
        return plainDataHandler

    @staticmethod
    def identifyStorages(plainDataHandler):
        persistent_type = plainDataHandler.persistent.type
        volatile_type = plainDataHandler.volatile.type
        persistent_class = persistent.import_class(persistent_type)
        volatile_class = volatile.import_class(volatile_type)
        return persistent_class, volatile_class

    def __init__(self, plainDataHandler, settings):
        plainDataHandler = self.inferAttributes(plainDataHandler)
        Persistent, Volatile = self.identifyStorages(plainDataHandler)
        self.persistent = Persistent(plainDataHandler.persistent, settings)
        self.volatile = Volatile(plainDataHandler.volatile, settings)

    @property
    def values(self):
        if not self.volatile.ready:
            if not self.persistent.path.allExist():
                pass  # ToDo: Raise exception.
            self.volatile.populate(self.persistent)
        return self.volatile.values

    @values.setter
    def values(self, newValue):
        if not self.persistent.path.anyExists():
            pass  # ToDo: Raise exception.
        self.volatile.mutate(self.persistent, newValue)

    def toDict(self):
        return {
            'persistent': self.persistent.toDict(),
            'volatile': self.volatile.toDict(),
        }
