import hail as hl

from ...base import Volatile


class Hail(Volatile):

    def populate(self, gateway):
        self.values, self.ready = hl.read_matrix_table(gateway, **self.importParameters), True

    def mutate(self, gateway, newValue):
        self.values, self.ready = newValue, True
        newValue.write(gateway, **self.exportParameters)

    def toDict(self):
        return {
            'spec': 'HailMatrixTable',
            'importParameters': self.importParameters,
            'exportParameters': self.exportParameters,
        }
