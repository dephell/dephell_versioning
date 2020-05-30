from ._core import bump_file, bump_version, get_aliases, get_rules, get_schemes
from ._schemes import BaseScheme, SCHEMES


__version__ = '0.1.2'


__all__ = [
    'BaseScheme',
    'bump_file',
    'bump_version',
    'get_aliases',
    'get_rules',
    'get_schemes',
    'SCHEMES',
]
