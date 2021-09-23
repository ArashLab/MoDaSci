class ExceptionBase(Exception):
    pass


class UnsupportedScheme(ExceptionBase):

    def __init__(self, scheme):
        super(UnsupportedScheme, self).__init__(f'"{scheme}" paths are not supported.')
        self.unsupportedScheme = scheme


class ModuleNotFound(ExceptionBase):

    def __init__(self, identifier, checked):
        li = '\n'.join(f' * {path}' for path in checked)
        super(ModuleNotFound, self).__init__(f'"{identifier}" could not be imported; expected to find it in:\n{li}')
        self.missingIdentifier = identifier
        self.checkedPaths = checked
