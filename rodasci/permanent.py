from .pathlist import PathList

class Permanent:

    def __init__(self, plainPermanent):
        self.pathList = PathList(plainPermanent.path)
        self.ready = plainPermanent.ready

    def __iter__(self):
        yield 'path', list(self.pathList)
        yield 'ready', self.ready

    