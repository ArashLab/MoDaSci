from munch import Munch

from . import persistents, volatiles
from .serialization import YAMLMixin


class DataHandler(YAMLMixin):

    @staticmethod
    def inferStorage(plainDataHandler):
        # ToDo: The inference logic is incomplete and only intended for tests.
        if isinstance(plainDataHandler.persistent, str):  # It's only a path.
            plainDataHandler.persistent = Munch({'path': plainDataHandler.persistent})
        persistent_format = plainDataHandler.persistent.get('format') or 'Reference'
        persistent_class = getattr(persistents, persistent_format)
        volatile_format = plainDataHandler.get('volatile', Munch({})).get('format') or 'HailTable'
        volatile_class = getattr(volatiles, volatile_format)
        return persistent_class, volatile_class

    def __init__(self, plainDataHandler):
        Persistent, Volatile = self.inferStorage(plainDataHandler)
        self.persistent = Persistent(plainDataHandler.get('persistent'))
        self.volatile = Volatile(plainDataHandler.get('volatile'))

    @property
    def values(self):
        if not self.volatile.ready:
            self.volatile.populate(self.persistent.readFrom)
        return self.volatile.values

    @values.setter
    def values(self, newValue):
        self.volatile.mutate(self.persistent.writeTo, newValue)

    def toDict(self):
        return {
            'persistent': self.persistent.toDict(),
            'volatile': self.volatile.toDict(),
        }
