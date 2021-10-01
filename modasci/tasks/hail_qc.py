from pydoc import HTMLDoc
from hail import table
from modasci.data_connector import DataConnector
from ..task import Task
import hail as hl

class HailQC(Task):

    def execute(self):
        mt = self.dataConnectors.mt.values
        axis = self.parameters.axis
        if axis == 'col':
            mt = hl.sample_qc(mt, name='qc')
        elif axis == 'row':
            mt = hl.variant_qc(mt, name='qc')
        self.dataConnectors.qc.values = mt.qc
