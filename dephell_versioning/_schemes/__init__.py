from types import MappingProxyType

from ._base import BaseScheme
from ._calver import CalVerScheme
from ._comver import ComVerScheme
from ._roman import RomanScheme
from ._semver import SemVerScheme
from ._serial import SerialScheme


__all__ = [
    'SCHEMES',

    'BaseScheme',
    'CalVerScheme',
    'ComVerScheme',
    'RomanScheme',
    'SemVerScheme',
    'SerialScheme',
]


SCHEMES = MappingProxyType(dict(
    calver=CalVerScheme(),
    comver=ComVerScheme(),
    roman=RomanScheme(),
    semver=SemVerScheme(),
    serial=SerialScheme(),
))
