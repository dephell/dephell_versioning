from typing import Union
from packaging.version import Version
from ._base import BaseScheme


class SerialScheme(BaseScheme):
    """
    https://packaging.python.org/guides/distributing-packages-using-setuptools/#serial-versioning
    """

    def bump_init(self, version: Union[Version, str]) -> str:
        return '1'

    def bump_major(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        return str(version.release[0] + 1)
