
from .permanent import Permanent
from .volatile import Volatile

class DataHandler:

    def __init__(self, dataHandleDict):
        self.permanent = Permanent(dataHandleDict.Permanent)
        self.volatile = Volatile(dataHandleDict.Volatile)

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
