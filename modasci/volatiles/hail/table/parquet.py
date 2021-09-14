import hail as hl

from ...base import Volatile


class Text(Volatile):

    def populate(self, gateway):
        pass
        #self.values, self.ready = hl.import_table(gateway, **self.importParameters), True

    def mutate(self, gateway, newValue):
        self.values, self.ready = newValue, True
        #newValue.export(gateway, **self.exportParameters)

    def toDict(self):
        return {
            'spec': 'HailTable',
            'importParameters': self.importParameters,
            'exportParameters': self.exportParameters,
        }
