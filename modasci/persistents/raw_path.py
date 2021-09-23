from contextlib import contextmanager

from ..persistent import Persistent


class RawPath(Persistent):
    """Raw reference to a persistent storage.

    References simply return the path to the storage as the gateways, leaving all required actions to the volatile
    counterpart. No more than a simple path is expected from the workflow description.
    """

    @contextmanager
    def read(self):
        yield self.path.plain()

    @contextmanager
    def write(self):
        yield self.path.plain()
