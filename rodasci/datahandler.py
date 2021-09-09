from .permanent import Permanent
from .volatile import Volatile

class DataHandler:

    def __init__(self, plainDataHandler):
        self.permanent = Permanent(plainDataHandler.Permanent)
        self.volatile = Volatile(plainDataHandler.Volatile)

    def __iter__(self):
        yield 'Permanent', dict(self.permanent)
        yield 'Volatile', dict(self.volatile)


    # @property
    # def permanent(self):
    #     return self.__permanent

    # @permanent.setter
    # def permanent(self, data):
    #     self.__permanent = data

    # @property
    # def volatile(self):
    #     return self.__volatile

    # @volatile.setter
    # def volatile(self, data):
    #     self.__volatile = data

    # def __PermanentToVolatile(self):
    #     pass

    # def __VolatileToPermanent(self):
    #     pass
