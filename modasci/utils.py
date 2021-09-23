from pydoc import locate

from stringcase import snakecase

from .exceptions import ModuleNotFound


def snake_case(string):
    """
    The module wraps around the function provided by `stringcase`, to solve its all-caps-issue!

    Parameters
    ----------
    string: str
        Identifier.

    Returns
    -------
    str
        String in `camel_case`.
    """
    return snakecase(string) if string.upper() != string else string.lower()


def import_class(directory, identifier):
    """Imports a class based on the passed strings.

    Parameters
    ----------
    directory: str
        Denotes the directory within the root of `modasci` in which the class may be found.
    identifier: str
        Locates the class in the following style: `[sub_package].<ClassName>`.

    Returns
    -------
    callable:
        The constructor for the class.

    Raises
    ------
    ModuleNotFound
        In case the class could not be imported from the expected location.
    """
    *sub_package, class_name = identifier.split('.')
    module = [directory, *sub_package, snake_case(class_name), class_name]
    packages = [[], ['modasci']]  # Sorted based on conflict resolution priority.
    paths = ['.'.join((*package, *module)) for package in packages]
    for path in paths:
        cls = locate(path)
        if cls is not None:
            return cls
    raise ModuleNotFound(identifier, paths)

