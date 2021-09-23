import hail as hl

from ...volatile import Volatile


class Table(Volatile):
    # I couldn't find corresponding export functions for the following file extension formats.
    # Perhaps, we could achieve this by first transforming them into a dataframe.
    # However, this might be reductive. We might expect users to bypass them explicitly.
    functions = {
        '.csv': ('import_table', ''),
        '.tsv': ('import_table', ''),
        '.bed': ('import_bed', ''),
        '.fam': ('import_fam', ''),
        '.int': ('import_locus_intervals', ''),  # Not so sure about the file extension format.
    }

    def populate(self, persistent):
        extension, compression = persistent.path.extension()
        read_func, write_func = self.functions[extension]
        with persistent.read() as handle:
            read_func = getattr(hl, read_func)
            dataFrame = read_func(handle, **self.importParameters)
        self.values, self.ready = dataFrame, True

    def mutate(self, persistent, updatedTable):
        extension, compression = persistent.path.extension()
        read_func, write_func = self.functions[extension]
        with persistent.write() as handle:
            write_func = getattr(updatedTable, write_func)
            write_func(handle, **self.exportParameters)
        self.values, self.ready = updatedTable, True
