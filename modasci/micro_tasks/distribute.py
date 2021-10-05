from ..micro_task import MicroTask

import hail as hl

class Distribute(MicroTask):

    def execute(self, volatileData):
        if isinstance(volatileData, hl.MatrixTable) or isinstance(volatileData, hl.Table):
            data = volatileData
            if 'coalesce' in self.parameters:
                data = data.naive_coalesce(self.parameters.coalesce)
            if 'repartition' in self.parameters:
                data = data.repartition(self.parameters.repartition)
            if 'persist' in self.parameters:
                if self.parameters.persis == 'cache':
                    data = data.cache()
                else:  
                    data = data.persist(self.parameters.persist)

        return data
