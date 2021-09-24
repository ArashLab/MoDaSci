import hail as hl

from ...volatile import Volatile


class Table(Volatile):
    # I couldn't find corresponding export functions for the following file extension formats.
    # Perhaps, we could achieve this by first transforming them into a dataframe.
    # However, this might be reductive. We might expect users to bypass them explicitly.
    functions = {
        '.csv': ('import_table', 'export', True),
        '.tsv': ('import_table', 'export', True),
        '.bed': ('import_bed', '', False),
        '.fam': ('import_fam', '', False),
        '.int': ('import_locus_intervals', '', False),  # Not so sure about the file extension format.
        '.ht': ('read_table', 'write', True)
    }

    def populate(self, persistent):
        extension, compression = persistent.path.extension()
        read_func, write_func, from_instance = self.functions[extension]
        with persistent.read() as handle:
            read_func = getattr(hl, read_func)
            dataFrame = read_func(handle, **self.importParameters)
        self.values, self.ready = dataFrame, True

    def mutate(self, persistent, updatedTable):
        extension, compression = persistent.path.extension()
        read_func, write_func, from_instance = self.functions[extension]
        with persistent.write() as handle:
            if from_instance:
                write_func = getattr(updatedTable, write_func)
                write_func(handle, **self.exportParameters)
            else:
                write_func = getattr(hl, write_func)
                write_func(updatedTable, handle, **self.exportParameters)
        self.values, self.ready = updatedTable, True
