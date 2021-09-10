class Volatile:

    def __init__(self, plianVolatile):
        self.format = plianVolatile.format
        self.ready = plianVolatile.ready

    def __iter__(self):
        yield 'format', self.format
        yield 'Ready', self.ready