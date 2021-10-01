from pydoc import HTMLDoc
from hail import table
from modasci.data_connector import DataConnector
from ..task import Task
import hail as hl

class HailUnion(Task):

    def execute(self):
        left = self.dataConnectors.left.values
        right = self.dataConnectors.right.values
        if isinstance(left, hl.MatrixTable) and isinstance(right, hl.MatrixTable):
            axis = self.parameters.axis
            if axis == 'col':
                how = self.parameters.get('how', 'inner')
                result = left.union_cols(right, row_join_type=how)
            elif axis == 'row':
                result = left.union_rows(right)
        elif isinstance(left, hl.Table) and isinstance(right, hl.Table):
            result = left.union(right)
        self.dataConnectors.result.values = result
