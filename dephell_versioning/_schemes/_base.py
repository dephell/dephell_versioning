from abc import ABC, abstractmethod
from types import MappingProxyType
from typing import Union, FrozenSet, Tuple

# external
from packaging.version import Version

from .._cached_property import cached_property


class BaseScheme(ABC):
    aliases = MappingProxyType(dict(
        breaking='major',
        feature='minor',
        fix='patch',
        micro='patch',

        prebreaking='premajor',
        prefeature='preminor',
        prefix='prepatch',
        premicro='prepatch',
    ))

    @cached_property
    def rules(self) -> FrozenSet[str]:
        rules = set()
        for method in dir(self):
            if method.startswith('bump_'):
                rules.add(method[5:])
        return frozenset(rules)

    def bump(self, version: Union[Version, str], rule: str) -> str:
        # explicitly specified local version
        if rule[0] == '+':
            if not hasattr(self, 'bump_local'):
                raise LookupError('unsupported rule: local')
            version = str(version).split('+')[0]
            return version + rule

        rule = self.aliases.get(rule, rule)
        method = getattr(self, 'bump_' + rule, None)
        if method is None:
            raise LookupError('unsupported rule: {}'.format(rule))
        return method(version=version)

    @abstractmethod
    def bump_init(self, version: Union[Version, str]) -> str:
        pass

    @abstractmethod
    def bump_major(self, version: Union[Version, str]) -> str:
        pass

    @staticmethod
    def _get_parts(version: Union[Version, str]) -> Tuple[int, ...]:
        if isinstance(version, str):
            version = Version(version)
        return version.release + (0, 0)

    def __repr__(self) -> str:
        return '{name}({rules})'.format(
            name=type(self).__name__,
            rules=', '.join(self.rules),
        )
