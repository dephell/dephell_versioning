from types import MappingProxyType

from ._base import BaseScheme
from ._roman import RomanScheme
from ._semver import SemVerScheme
from ._serial import SerialScheme


__all__ = [
    'SCHEMES',

    'BaseScheme',
    'RomanScheme',
    'SerialScheme',
]


SCHEMES = MappingProxyType(dict(
    roman=RomanScheme(),
    semver=SemVerScheme(),
    serial=SerialScheme(),
))
