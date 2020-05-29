from typing import Union
from packaging.version import Version
from ._semver import SemVerScheme


class PEPScheme(SemVerScheme):
    """
    https://www.python.org/dev/peps/pep-0440/#version-scheme
    """

    _alpha = 'alpha'
    _beta = 'beta'
    _rc = 'rc'  # PEP has different pre-release syntax

    pre_mapping=dict(
        a=_alpha,
        b=_beta,
        rc=_rc
    )
    def bump_pre(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        if version.pre:
            pre = version.pre[1]
            return '{}.{}.{}{}{}'.format(*parts[:3],self.pre_mapping[version.pre[0]], pre+1)
        else:
            return '{}.{}.{}{}{}'.format(*parts[:3], self._alpha, 1)

    def bump_alpha(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        alpha = version.pre[1] if (version.pre and version.pre[0] == 'a') else 0
        return '{}.{}.{}{}{}'.format(*parts[:3], self._alpha, alpha+1)

    def bump_beta(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        beta = version.pre[1] if (version.pre and version.pre[0] == 'b') else 0
        return '{}.{}.{}{}{}'.format(*parts[:3], self._beta, beta+1)

    def bump_rc(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)
        parts = self._get_parts(version)
        rc = version.pre[1] if (version.pre and version.pre[0] == 'rc') else 0
        return '{}.{}.{}{}{}'.format(*parts[:3], self._rc, rc+1)


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
        post = (version.post or 0) + 1  # type: ignore
        return '{}.{}.{}.post{}'.format(*parts[:3], post)

    def bump_dev(self, version: Union[Version, str]) -> str:
        if isinstance(version, str):
            version = Version(version)

        suffix = ''
        if version.pre:
            suffix += 'rc{}'.format(version.pre[1])
        elif version.post:
            suffix += '.post{}'.format(version.post)
        dev = (version.dev or 0) + 1  # type: ignore
        suffix += '.dev{}'.format(dev)

        parts = self._get_parts(version)
        return '{}.{}.{}{}'.format(*parts[:3], suffix)
