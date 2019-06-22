from types import MappingProxyType

from ._base import BaseRule
from ._roman import RomanRule
from ._serial import SerialRule


__all__ = [
    'RULES',

    'BaseRule',
    'RomanRule',
    'SerialRule',
]


RULES = MappingProxyType(dict(
    roman=RomanRule(),
    serial=SerialRule(),
))
