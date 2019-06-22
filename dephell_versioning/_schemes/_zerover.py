from typing import Union
from packaging.version import Version
from ._semver import SemVerScheme


class ZeroVerScheme(SemVerScheme):

    @staticmethod
    def _get_parts(version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        return (0, ) + version.release[1:] + (0, 0)
