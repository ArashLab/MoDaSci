from ..task import Task


class Bypass(Task):

    def execute(self):
        conversions = {
            ('DataFrame', 'Table'): self.dataframe_to_table,
            # The rest will follow here.
        }
        # Might want to catch the possible KeyError exception in the following statement and raise an appropriate error.
        convert = conversions[(self.dataConnectors.source.name, self.dataConnectors.destination.name)]
        self.dataConnectors.destination.values = convert(self.dataConnectors.source.values)

    # Since we aren't going to list the optional dependencies in `requirements.txt` or other recognized locations, IDEs
    # will warn us about this. The following comment line disables this behaviour in most IDEs.
    # noinspection PyPackageRequirements
    @staticmethod
    def dataframe_to_table(dataframe):
        try:
            # Imports are localized and therefore, importing this module while not having all the dependencies wouldn't
            # cause an exception.
            import pandas as pd
            import hail as hl
        except ImportError:
            print('better raise an appropriate exception')  # ToDo
        else:
            return hl.Table.from_pandas(dataframe)
