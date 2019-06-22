from typing import Union
from packaging.version import Version
from ._semver import SemVerScheme


class PEPScheme(SemVerScheme):
    _rc = 'rc'  # PEP has different pre-release syntax

    def bump_local(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        old = str(version).split('+')[0]
        local = int(version.local) if version.local else 0
        return '{}+{}'.format(old, local + 1)

    def bump_release(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        suffix = ''
        if version.post:
            suffix += '.post{}'.format(version.post)
        if version.dev:
            suffix += '.dev{}'.format(version.dev)
        parts = self._get_parts(version)
        return '{}.{}.{}{}'.format(*parts[:3], suffix)

    # pep-specific rules, unsupported by semver

    def bump_post(self, version: Union[Version, str]) -> str:
        # PEP allows post-releases for pre-releases,
        # but it "strongly discouraged". So, let's ignore it.
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        return '{}.{}.{}.post{}'.format(*parts[:3], (version.post or 0) + 1)

    def bump_dev(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)

        suffix = ''
        if version.pre:
            suffix += 'rc{}'.format(version.pre[1])
        elif version.post:
            suffix += '.post{}'.format(version.post)
        suffix += '.dev{}'.format((version.dev or 0) + 1)

        parts = self._get_parts(version)
        return '{}.{}.{}{}'.format(*parts[:3], suffix)
