from ..micro_task import MicroTask

import hail as hl
import pandas as pd
import numpy as np

# ToDo: add all other libraries needed to be available for the user code

class Evaluate(MicroTask):

    def execute(self, volatileData):
        data = eval(self.parameters.exprssion, locals={'data': volatileData})
        return data
        