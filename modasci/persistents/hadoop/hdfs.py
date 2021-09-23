from contextlib import contextmanager

import pydoop.hdfs as hdfs

from ...persistent import Persistent


class HDFS(Persistent):
    """Enables access to `hdfs://*` files.

    The module uses `pydoop` and allows access to the target file through a stream.
    """

    @contextmanager
    def read(self, binary=False):
        with hdfs.open(self.path.plain(), mode='rb' if binary else 'r') as handler:
            yield handler

    @contextmanager
    def write(self, binary=False):
        with hdfs.open(self.path.plain(), mode='wb' if binary else 'w') as handler:
            yield handler
