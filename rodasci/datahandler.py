from typing_extensions import ParamSpecArgs
from .permanent import Permanent
from .volatile import Volatile

class DataHandler:

    def __init__(self, plainDataHandler):
        self.__permanent = Permanent(plainDataHandler.permanent)
        self.__volatile = Volatile(plainDataHandler.volatile)

    def __iter__(self):
        yield 'permanent', dict(self.permanent)
        yield 'volatile', dict(self.volatile)


    @property
    def permanent(self):
        return self.__permanent

    @permanent.setter
    def permanent(self, data):
        self.__permanent = data

    @property
    def volatile(self):
        if not self.__volatile.ready:
            self.__PermanentToVolatile()
        return self.__volatile

    @volatile.setter
    def volatile(self, dataset):
        #self.__volatile = data
        pass

    def __PermanentToVolatile(self):
        pass

    def __VolatileToPermanent(self):
        pass
