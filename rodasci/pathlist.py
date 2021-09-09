from .pathdict import PathDict

class PathList:

    def __init__(self, pathList):
        self.pathList = pathList

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
 