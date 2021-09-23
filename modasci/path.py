import os
import urllib.parse
from typing import Union, Optional

import requests
from munch import Munch

from .exceptions import UnsupportedScheme


class Path:
    """Represents a path to a storage.

    The path can represent one or more physical paths, which can be accessed through various schemes. Schemes can be
    file, http, https, ftp, s3, etc.

    Attributes
    ----------
    self.raw: Union[str, list, dict, Munch]
        The `plainPath` that the instance is based on. This attribute might be removed in future.
    singular: bool
        Specifies whether the instance contains more than a path. This could be True when the passed `plainPath` was a
        list or a dict.
    parsed: dict
        Contains the parsed versions of the paths, where the keys are either user defined or are index-based.

    Parameters
    ----------
    plainPath: Union[str, list, dict, Munch]
        The path as it is defined in the workflow.
    """

    def __init__(self, plainPath, settings):
        self.localMode = settings.localMode
        self.defaultPathScheme = settings.defaultPathScheme
        self.singular = isinstance(plainPath, str)  # Otherwise, it would be a `list` or a `dict`.
        plainPath = plainPath if not self.singular else [plainPath]  # Ensure that `plainPath` is iterable.
        plainPath = plainPath if isinstance(plainPath, dict) else {index: path for index, path in enumerate(plainPath)}  # Ensure that `plainPath` is a `dict`.
        self.parsed = {label: self.parse(path, settings.defaultPathScheme) for label, path in plainPath.items()}
        self.raw = plainPath

    @staticmethod
    def parse(path, defaultScheme):
        path = os.path.expandvars(path)
        parse_result = urllib.parse.urlparse(path)
        if not parse_result.scheme:
            # noinspection PyProtectedMember
            parse_result = parse_result._replace(scheme=defaultScheme)
        return parse_result

    @staticmethod
    def exists(url, parsed):
        """Checks whether a url points to an existing resource.

        The function handles different schemes internally.

        Parameters
        ----------
        url: str
            Raw URL.
        parsed: urllib.parse.ParseResult
            The URL, parsed using `urllib.parse.urlparse()`.

        Returns
        -------
        bool
        """
        if parsed.scheme == 'file':
            return os.path.exists(parsed.path)
        elif parsed.scheme in ('http', 'https'):
            return requests.head(url).ok
        # ToDo: Other allowed URL schemes.
        raise UnsupportedScheme(parsed.scheme)

    def anyExists(self):
        return any(self.exists(url, parsed) for url, parsed in zip(self.raw.values(), self.parsed.values()))

    def allExist(self):
        return all(self.exists(url, parsed) for url, parsed in zip(self.raw.values(), self.parsed.values()))

    def plain(self):
        """Transforms the internal values into readable path(s).

        Returns
        -------
        Union[str, list]
            A single path, or a list of paths.
        """
        asList = [parsed.path if self.localMode and parsed.scheme == self.defaultPathScheme else url
                  for url, parsed in zip(self.raw.values(), self.parsed.values())]
        return asList if len(asList) > 1 else asList[0]

    def labeled(self):
        """Transforms the internal values into readable paths.

        Returns
        -------
        dict
            The keys represent the labels assigned to the paths by the user, or automatically generated, while the
            values contain the actual paths, which could have been separately extracted using `.plain()`.
        """
        return {label: (parsed.path if self.localMode and parsed.scheme == self.defaultPathScheme else url)
                for (label, url), parsed in zip(self.raw.items(), self.parsed.values())}

    def extension(self):
        """The extension of the designated path. The method will return a tuple if the path is singular, and a list of
        tuples otherwise.

        Returns
        -------
        extension: str
            Original file extension.
        compression: Optional[str]
            Compression extension.
        """
        asList = []
        for label, parsed in self.parsed.items():
            (remainder, extension), compression = os.path.splitext(parsed.path), None
            compressed = extension in ('.7z', '.gz', '.bgz', '.lz')  # ToDo: Extend this list.
            if compressed is True:
                compression = extension
                remainder, extension = os.path.splitext(remainder)
            asList.append((extension, compression))
        return asList if len(asList) > 1 else asList[0]
