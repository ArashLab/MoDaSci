class Volatile:

    def __init__(self, plianVolatile):
        self.memory = plianVolatile.Memory
        self.ready = plianVolatile.Ready

    def __iter__(self):
        yield 'PathList', self.memory
        yield 'Ready', self.ready