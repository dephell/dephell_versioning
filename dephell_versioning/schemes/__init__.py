from types import MappingProxyType

from ._base import BaseScheme
from ._roman import RomanScheme
from ._serial import SerialScheme


__all__ = [
    'RULES',

    'BaseScheme',
    'RomanScheme',
    'SerialScheme',
]


SCHEMES = MappingProxyType(dict(
    roman=RomanScheme(),
    serial=SerialScheme(),
))
