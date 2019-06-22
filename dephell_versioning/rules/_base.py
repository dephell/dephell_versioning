from abc import ABC, abstractmethod
from typing import Union, FrozenSet

# external
from packaging.version import Version

from .._cached_property import cached_property


class BaseRule(ABC):
    aliases = dict(
        breaking='major',
        feature='minor',
        fix='patch',
        micro='patch',

        rc='pre',
        alpha='pre',
        beta='pre',

        prebreaking='premajor',
        prefeature='preminor',
        prefix='prepatch',
        premicro='prepatch',
    )

    @cached_property
    def rules(self) -> FrozenSet[str]:
        rules = set()
        for method in self.__dict__:
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
