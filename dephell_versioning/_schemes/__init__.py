from types import MappingProxyType

from ._base import BaseScheme
from ._calver import CalVerScheme
from ._comver import ComVerScheme
from ._roman import RomanScheme
from ._semver import SemVerScheme
from ._serial import SerialScheme
from ._zerover import ZeroVerScheme


__all__ = [
    'SCHEMES',

    'BaseScheme',
    'CalVerScheme',
    'ComVerScheme',
    'RomanScheme',
    'SemVerScheme',
    'SerialScheme',
    'ZeroVerScheme',
]


SCHEMES = MappingProxyType(dict(
    calver=CalVerScheme(),
    comver=ComVerScheme(),
    roman=RomanScheme(),
    romver=SemVerScheme(),  # RomVer is an alias for SemVer
    semver=SemVerScheme(),
    serial=SerialScheme(),
    serover=ZeroVerScheme(),
))
