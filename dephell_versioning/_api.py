from typing import FrozenSet, Union
from packaging.version import Version
from ._schemes import BaseScheme, SCHEMES


def get_schemes() -> FrozenSet[str]:
    return frozenset(SCHEMES)


def get_rules() -> FrozenSet[str]:
    rules = set()
    for scheme in SCHEMES.values():
        rules.update(scheme.rules)
    return frozenset(rules)


def get_aliases() -> FrozenSet[str]:
    return frozenset(BaseScheme.aliases)


def bump_version(version: Union[Version, str], rule: str, scheme: str = 'semver') -> str:
    scheme_manager = SCHEMES.get(scheme)
    if scheme_manager is None:
        raise LookupError('invalid scheme: {}'.format(scheme))
    return scheme_manager.bump(version=version, rule=rule)
