### To access version
import importlib.resources
from pathlib import Path

packageName='rodasci'
moduleName='path'
with importlib.resources.path(packageName, 'VERSION') as path:
    print(path)
    moduleVersion = Path(path).read_text()

if __name__ == '__main__':
    print(f'This is `{packageName}.{moduleName}` version `{moduleVersion}`')
    print('This module is not executable.')
    exit(0)

### dict like class
class PathDict:

    @classmethod
    def Init(cls, defaultFileSystem='file://', defaultMode=False):
        cls.defaultFileSystem = defaultFileSystem
        cls.defaultMode = defaultMode

    def __init__(self, data):
        self.pathDict = data
        pass

    @property
    def pathDict(self):
        return self.__pathDict

    @pathDict.setter ### Should be called once only
    def pathDict(self, data):
        if isinstance(data, str):
            inferredDict = self.FullInfer(data)
        elif isinstance(data, dict):
            inferredDict = self.Infer(data)
        else:
            pass ### Error
        self.__pathDict.update(inferredDict)

    def FullInfer(self, data):
        self.pathDict = data
        pass ### infer from string

    def Infer(self, data):
        self.pathDict = data
        pass ### infer from object

    def Exist(self):
        pass

### list like class
class PathList:

    def __init__(self, data=None):
        if data:
            self.pathList = data

    @property
    def pathList(self):
        return self.__pathList

    @pathList.setter
    def pathList(self, data):
        self.__processed = False
        if isinstance(data, str):
            self.__pathList = [data]
        elif isinstance(data, dict):
            self.__pathList = [data]
        elif isinstance(data, list):
            self.__pathList = data
        else:
            pass ### Error

    @property
    def pathDictAll(self):
        return self.__pathDictAll

    @property
    def path(self):
        if len(self.pathList) != 1:
            pass #Error
        return self.pathList[0].path

    @property
    def paths(self):
        return [item.path for item in self.pathList]

    def Process(self):
        newList = list()
        for item in self.pathList:
            tempList = self.ToPathDict(item)
            newList.extend(tempList)

        self.pathList = newList
        self.__processed = True

    def ToPathDict(self, data):
        return [] ### list of AbPathDict

    def ExistAll(self): # only if processed
        if not self.__processed:
            pass ### Error

        all([item.Exist() for item in self.pathList])

    def ExistAny(self):
        if not self.__processed:
            pass ### Error

        any([item.Exist() for item in self.pathList])

    def Exist(self):
        self.ExistAll()

    def FindAllDict(self):
        allDict = 'something' ### TBI
        self.__pathDictAll = PathDict(allDict)
 