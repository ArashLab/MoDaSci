import pandas as pd

from ..base import Volatile


class Parquet(Volatile):
    """Volatile proxy for pandas dataframes.

    This class can work in conjunction with: `Reference`.
    """

    def populate(self, gateway):
        pass
        #self.values, self.ready = pd.read_csv(gateway, **self.importParameters), True
    
    def mutate(self, gateway, newValue):
        self.values, self.ready = newValue, True
        #newValue.to_csv(gateway, **self.exportParameters)

    def toDict(self):
        return {
            'spec': 'PandasDataFrame',
            'importParameters': self.importParameters,
            'exportParameters': self.exportParameters,
        }
