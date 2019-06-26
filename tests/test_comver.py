import pytest

from dephell_versioning import bump_version


@pytest.mark.parametrize('rule, old, new', [
    ('init', '', '0.1'),
    ('major', '1.2', '2.0'),
    ('minor', '1.2', '1.3'),

    # special part
    ('pre',   '1.2', '1.2-rc.1'),
    ('local', '1.2', '1.2+1'),

    # bump special part
    ('pre',   '1.2-rc.1', '1.2-rc.2'),
    ('local', '1.2+1', '1.2+2'),

    # release
    ('release', '1.2', '1.2'),
    ('release', '1.2-rc.1', '1.2'),
    ('release', '1.2+1', '1.2'),
    ('release', '1.2-rc.1+1', '1.2'),
])
def test_bump_version(rule, old, new):
    assert bump_version(rule=rule, version=old, scheme='comver') == new
