from typing import Union
from packaging.version import Version
from ._base import BaseScheme


class ComVerScheme(BaseScheme):
    """
    https://github.com/staltz/comver
    """

    def bump_init(self, version: Union[Version, str]) -> str:
        return '0.1'

    def bump_major(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        return '{}.0'.format(parts[0] + 1)

    def bump_minor(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        return '{}.{}'.format(parts[0], parts[1] + 1)

    def bump_pre(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = version.release + (0, 0)
        pre = version.pre[1] if version.pre else 0
        return '{}.{}-rc.{}'.format(*parts[:2], pre + 1)

    def bump_local(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = version.release + (0, 0)
        pre = '-{}.{}'.format(*version.pre) if version.pre else ''
        local = int(version.local) if version.local else 0
        return '{}.{}{}+{}'.format(*parts[:2], pre, local + 1)

    def bump_premajor(self, version: Union[Version, str]) -> str:
        return self.bump_major(version=version) + '-rc.1'

    def bump_preminor(self, version: Union[Version, str]) -> str:
        return self.bump_minor(version=version) + '-rc.1'

    def bump_release(self, version: Union[Version, str]) -> str:
        parts = self._get_parts(version)
        return '{}.{}'.format(*parts[:2])
