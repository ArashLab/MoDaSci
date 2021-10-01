from pydoc import HTMLDoc
from hail import table
from modasci.data_connector import DataConnector
from ..task import Task
import hail as hl

class HailJoin(Task):

    def execute(self):
        left = self.dataConnectors.left.values
        right = self.dataConnectors.right.values
        how = self.parameters.how
        if isinstance(left, hl.MatrixTable) and isinstance(right, hl.Table):
            axis = self.parameters.axis
            if how in ['semi', 'anti']:
                func = getattr(left, f'{how}_join_{axis}s')
                result = func(right)
            if how == 'annotate':
                if axis in ['row', 'col']:
                   expr = {self.parameters.name: right[getattr(left, f'{axis}_key')]}
                   func = getattr(left, f'annotate_{axis}s')
                   result = func(**expr)

        elif isinstance(left, hl.Table) and isinstance(right, hl.Table):
            if how == 'semi':
                result = left.semi_join(right)
            elif how == 'anti':
                result = left.anti_join(right)
            elif how == 'annotate':
                expr = {self.parameters.name: right[left.key]}
                result = left.annotate(**expr)
            elif how in ['inner', 'outter', 'left', 'right']:
                result = left.join(right, how=how)
        self.dataConnectors.result.values = result
