from .dataset import Dataset

class Volatile:

    def __init__(self, plianVolatile):
        self.dataset = Dataset(plianVolatile.dataset)
        self.ready = plianVolatile.ready

    def __iter__(self):
        yield 'dataset', dict(self.dataset)
        yield 'Ready', self.ready

    @property
    def data(self):
        if not self.ready:
            self.ready
        pass

    @data.setter
    def data(self, data):
        ### write data to permanent
        pass