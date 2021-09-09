from typing import ValuesView


class PathDict:

    @classmethod
    def Init(cls, defaultFileSystem='file://', defaultMode=False):
        cls.defaultFileSystem = defaultFileSystem
        cls.defaultMode = defaultMode

    def __init__(self, plainPathDict):
        self.pathDict = plainPathDict
        pass

    def __iter__(self):
        for key, value in self.pathDict.items():
            yield key, value

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
