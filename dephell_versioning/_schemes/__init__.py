from types import MappingProxyType

from ._base import BaseScheme
from ._calver import CalVerScheme
from ._comver import ComVerScheme
from ._pep import PEPScheme
from ._roman import RomanScheme
from ._romver import RomVerScheme
from ._semver import SemVerScheme
from ._serial import SerialScheme
from ._zerover import ZeroVerScheme


__all__ = [
    'SCHEMES',

    'BaseScheme',
    'CalVerScheme',
    'ComVerScheme',
    'PEPScheme',
    'RomanScheme',
    'RomVerScheme',
    'SemVerScheme',
    'SerialScheme',
    'ZeroVerScheme',
]


SCHEMES = MappingProxyType(dict(
    calver=CalVerScheme(),
    comver=ComVerScheme(),
    pep=PEPScheme(),
    roman=RomanScheme(),
    romver=RomVerScheme(),
    semver=SemVerScheme(),
    serial=SerialScheme(),
    serover=ZeroVerScheme(),
))
