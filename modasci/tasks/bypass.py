from numpy import e
from modasci import utils
from ..task import Task

import hail as hl
import pandas as pd

class Bypass(Task):

    def execute(self):
        self.dataConnectors.destination.values = self.dataConnectors.source.values
