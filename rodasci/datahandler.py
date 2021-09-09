
### To access version
import importlib.resources
from pathlib import Path

packageName='rodasci'
moduleName='logger'
with importlib.resources.path(packageName, 'VERSION') as path:
    print(path)
    moduleVersion = Path(path).read_text()

if __name__ == '__main__':
    print(f'This is `{packageName}.{moduleName}` version `{moduleVersion}`')
    print('This module is not executable.')
    exit(0)

from .path import PathList

class Storage:
    
    def __init__(self):
        self.__ready = False
    
    @property
    def ready(self):
        return self.__ready

    @ready.setter
    def ready(self, data):
        self.__ready = data

class Volatile(Storage):
    pass

class Permanent(Storage):

    def __init__(self, data):
        self.pathList = PathList(data)

class DataHandler:

    def __init__(self, dataHandle):
        self.permanent = Permanent(dataHandle.volatile)
        self.volatile = Volatile(dataHandle.volatile)

    @property
    def permanent(self):
        return self.__permanent

    @permanent.setter
    def permanent(self, data):
        self.__permanent = data

    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, data):
        self.__volatile = data

    def __PermanentToVolatile(self):
        pass

    def __VolatileToPermanent(self):
        pass
