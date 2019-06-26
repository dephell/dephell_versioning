from datetime import date
from typing import Union
from packaging.version import Version
from ._base import BaseScheme


class CalVerScheme(BaseScheme):
    """
    https://calver.org/
    """

    # make it possible to reload date from child classes
    @property
    def today(self):
        return date.today()

    def bump_init(self, version: Union[Version, str]) -> str:
        return self.bump_major(version=version)

    def bump_major(self, version: Union[Version, str]) -> str:
        today = self.today
        return '{}.{}'.format(today.year, today.month)

    def bump_patch(self, version: Union[Version, str]) -> str:
        today = self.today
        if isinstance(version, str):
            version = Version(version)

        if version.release[0] == today.year and version.release[1] == today.month:
            micro = (version.release + (0, 0))[2]
            micro = today.day if micro < today.day else micro + 1
        else:
            micro = today.day
        return '{}.{}.{}'.format(today.year, today.month, micro)
