from .pathlist import PathList

class Permanent:

    def __init__(self, plainPermanent):
        self.pathList = PathList(plainPermanent.PathList)
        self.ready = plainPermanent.Ready

    def __iter__(self):
        yield 'PathList', list(self.pathList)
        yield 'Ready', self.ready