import pandas as pd

from ...volatile import Volatile


class DataFrame(Volatile):
    functions = {
        '.h5': ('read_hdf', 'to_hdf'),
        '.csv': ('read_csv', 'to_csv'),
        '.xml': ('read_xml', 'to_xml'),
        '.json': ('read_json', 'to_json'),
        '.html': ('read_html', 'to_html'),
        '.xls': ('read_excel', 'to_excel'),
        '.xlsx': ('read_excel', 'to_excel'),
        '.pickle': ('read_pickle', 'to_pickle'),
        '.parquet': ('read_parquet', 'to_parquet'),
    }

    def populate(self, persistent):
        extension, compression = persistent.path.extension()
        read_func, write_func = self.functions[extension]
        with persistent.read() as handle:
            read_func = getattr(pd, read_func)
            dataFrame = read_func(handle, **self.importParameters)
        self.values, self.ready = dataFrame, True

    def mutate(self, persistent, updatedDataFrame):
        extension, compression = persistent.path.extension()
        read_func, write_func = self.functions[extension]
        with persistent.write() as handle:
            write_func = getattr(updatedDataFrame, write_func)
            write_func(handle, **self.exportParameters)
        self.values, self.ready = updatedDataFrame, True
