class Dataset:

    def __init__(self, plianDataset):
        self.format = plianDataset.format

    def __iter__(self):
        yield 'format', self.format

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
       self.__data = data
       self.format = type(data) ###TBI