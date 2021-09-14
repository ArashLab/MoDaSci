import hail as hl

from ...base import Volatile


class PlinkBfile(Volatile):

    def populate(self, gateway):
        self.values, self.ready = hl.import_plink(gateway, **self.importParameters), True

    def mutate(self, gateway, newValue):
        self.values, self.ready = newValue, True
        newValue.export_plink(gateway, **self.exportParameters)

    def toDict(self):
        return {
            'spec': 'HailMatrixTableVCF',
            'importParameters': self.importParameters,
            'exportParameters': self.exportParameters,
        }
