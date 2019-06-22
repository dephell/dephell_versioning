import pytest

from dephell_versioning import bump_version


@pytest.mark.parametrize('rule, old, new', [
    ('init', '', '1'),
    ('major', '1', '2'),
    ('major', '3', '4'),
    ('major', '356', '357'),
])
def test_bump_version(rule, old, new):
    assert bump_version(rule=rule, version=old, scheme='serial') == new
