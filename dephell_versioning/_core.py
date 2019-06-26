import re
from pathlib import Path
from typing import FrozenSet, Union, Set, Iterable

from packaging.version import Version, VERSION_PATTERN

from ._schemes import BaseScheme, SCHEMES


REX_VERSION = re.compile(VERSION_PATTERN, re.VERBOSE | re.IGNORECASE)
PREFIXES = {'__version__', 'VERSION', 'version'}


def get_schemes() -> FrozenSet[str]:
    return frozenset(SCHEMES)


def get_rules(scheme: str = None) -> FrozenSet[str]:
    if scheme is not None:
        return SCHEMES[scheme].rules

    rules = set()  # type: Set[str]
    for scheme in SCHEMES.values():
        rules.update(scheme.rules)
    return frozenset(rules)


def get_aliases(rules: Iterable[str] = None) -> FrozenSet[str]:
    if rules is None:
        return frozenset(BaseScheme.aliases)

    result = set()  # type: Set[str]
    for alias, rule in BaseScheme.aliases.items():
        if rule in rules:
            result.add(alias)
    return frozenset(result)


def bump_version(version: Union[Version, str], rule: str, scheme: str = 'semver') -> str:
    scheme_manager = SCHEMES.get(scheme)
    if scheme_manager is None:
        raise LookupError('invalid scheme: {}'.format(scheme))
    return scheme_manager.bump(version=version, rule=rule)


def bump_file(path: Path, old: str, new: str) -> bool:
    file_bumped = False
    new_content = []
    with path.open('r') as stream:
        for line in stream:
            prefix, sep, _version = line.partition('=')
            if not sep:
                new_content.append(line)
                continue
            if prefix.rstrip() not in PREFIXES:
                new_content.append(line)
                continue

            # replace old version
            if old:
                new_line = line.replace(old, new, 1)
                if new_line != line:
                    new_content.append(new_line)
                    file_bumped = True
                    continue

            # replace any version
            new_line, count = REX_VERSION.subn(new, line)
            if count == 1:
                new_content.append(new_line)
                file_bumped = True
                continue

            new_content.append(line)
    if file_bumped:
        path.write_text(''.join(new_content))
    return file_bumped
