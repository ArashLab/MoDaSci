from .dataset import Dataset

class Volatile:

    def __init__(self, plianVolatile):
        self.dataset = Dataset(plianVolatile.dataset)
        self.ready = False

    def __iter__(self):
        yield 'dataset', dict(self.__dataset)
        yield 'Ready', self.ready

    @property
    def dataset(self):
        if not self.ready:

        pass

    @dataset.setter
    def dataset(self, dataset):
        ### write data to permanent
        pass