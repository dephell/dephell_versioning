from typing import Union
from packaging.version import Version
from .schemes import SCHEMES


def bump_version(version: Union[Version, str], rule: str, scheme: str = 'semver') -> str:
    scheme_manager = SCHEMES.get(scheme)
    if scheme_manager is None:
        raise LookupError('invalid scheme: {}'.format(scheme))
    return scheme_manager.bump(version=version, rule=rule)
