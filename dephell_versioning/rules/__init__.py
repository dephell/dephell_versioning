from types import MappingProxyType

from ._base import BaseRule
from ._roman import RomanRule


__all__ = [
    'RULES',

    'BaseRule',
    'RomanRule',
]


RULES = MappingProxyType(dict(
    roman=RomanRule,
))
