import pytest

from dephell_versioning import bump_version, SCHEMES


@pytest.mark.parametrize('rule, old, new', [
    ('init', '', 'I'),
    ('major', 'I', 'II'),
    ('major', 'IV', 'V'),
    ('major', 'V', 'VI'),
    ('major', 'X', 'XI'),
    ('major', 'XII', 'XIII'),
    ('major', 'XIII', 'XIV'),
])
def test_bump_version(rule, old, new):
    assert bump_version(rule=rule, version=old, scheme='roman') == new


@pytest.mark.parametrize('arabic, roman', [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),

    (10, 'X'),
    (13, 'XIII'),
    (14, 'XIV'),
    (15, 'XV'),
    (16, 'XVI'),

    (20, 'XX'),
    (24, 'XXIV'),
    (25, 'XXV'),
    (26, 'XXVI'),

    (994, 'CMXCIV'),
    (1995, 'MCMXCV'),
    (2015, 'MMXV'),
    (3986, 'MMMCMLXXXVI'),
])
def test_roman(arabic, roman):
    assert SCHEMES['roman'].arabic2roman(arabic) == roman
    assert SCHEMES['roman'].roman2arabic(roman) == arabic
