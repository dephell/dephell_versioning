from typing import Union
from packaging.version import Version
from ._base import BaseScheme


class SemVerScheme(BaseScheme):
    """
    https://semver.org/
    """

    _rc = '-rc.'  # make it possible to chenge pre-release syntax for PEP

    def bump_init(self, version: Union[Version, str]) -> str:
        return '0.1.0'

    def bump_major(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        parts = (parts[0] + 1, 0, 0)
        return '{}.{}.{}'.format(*parts)

    def bump_minor(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        parts = (parts[0], parts[1] + 1, 0)
        return '{}.{}.{}'.format(*parts)

    def bump_patch(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        parts = (parts[0], parts[1], parts[2] + 1)
        return '{}.{}.{}'.format(*parts)

    def bump_pre(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        pre = version.pre[1] if version.pre else 0
        return '{}.{}.{}{}{}'.format(*parts[:3], self._rc, pre + 1)

    def bump_local(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        pre = '-{}.{}'.format(*version.pre) if version.pre else ''
        local = int(version.local) if version.local else 0
        return '{}.{}.{}{}+{}'.format(*parts[:3], pre, local + 1)

    def bump_premajor(self, version: Union[Version, str]) -> str:
        new_version = self.bump_major(version=version)
        return self.bump_pre(version=new_version)

    def bump_preminor(self, version: Union[Version, str]) -> str:
        new_version = self.bump_minor(version=version)
        return self.bump_pre(version=new_version)

    def bump_prepatch(self, version: Union[Version, str]) -> str:
        new_version = self.bump_patch(version=version)
        return self.bump_pre(version=new_version)

    def bump_release(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        return '{}.{}.{}'.format(*parts[:3])
