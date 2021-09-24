import hail as hl

from ...volatile import Volatile


class MatrixTable(Volatile):
    functions = {
        '.vcf': ('import_vcf', 'export_vcf', False),
        '.bgen': ('import_bgen', 'export_bgen', False),
        '.gen': ('import_gen', 'export_gen', False),
        '.gvcf': ('import_gvcfs', '', False),  # Corresponding export method hasn't been introduced.
        'plink': ('import_plink', 'export_plink', False),
        '.mt': ('read_matrix_table', 'write', True),
    }

    def populate(self, persistent):
        extensions = persistent.path.extension()
        if isinstance(extensions, tuple):
            extension, compression = extensions
        elif isinstance(extensions, list):  # In case more than one path was listed.
            # Since `bim` is unique to PLINK datasets, we only check against that.
            if 'bim' in [extension for extension, compression in extensions]:
                extension, compression = 'plink', None
        # By this point, if the file is unknown, `extension` would be undefined, which will cause an extension. However,
        # we might want to catch it and raise a more appropriate error.
        read_func, write_func, from_instance = self.functions[extension]
        with persistent.read() as handle:
            read_func = getattr(hl, read_func)
            dataFrame = read_func(handle, **self.importParameters)
        self.values, self.ready = dataFrame, True

    def mutate(self, persistent, updatedMatrixTable):
        extensions = persistent.path.extension()
        if isinstance(extensions, tuple):
            extension, compression = extensions
        elif isinstance(extensions, list):  # In case more than one path was listed.
            # Since `bim` is unique to PLINK datasets, we only check against that.
            if 'bim' in [extension for extension, compression in extensions]:
                extension, compression = 'plink', None
        # By this point, if the file is unknown, `extension` would be undefined, which will cause an extension. However,
        # we might want to catch it and raise a more appropriate error.
        read_func, write_func, from_instance = self.functions[extension]
        with persistent.write() as handle:
            if from_instance:
                write_func = getattr(updatedMatrixTable, write_func)
                write_func(handle, **self.exportParameters)
            else:
                write_func = getattr(hl, write_func)
                write_func(updatedMatrixTable, handle, **self.exportParameters)
        self.values, self.ready = updatedMatrixTable, True
