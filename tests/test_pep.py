import pytest

from dephell_versioning import bump_version


@pytest.mark.parametrize('rule, old, new', [
    ('init', '', '0.1.0'),

    # base version
    ('major',    '1.2.3', '2.0.0'),
    ('minor',    '1.2.3', '1.3.0'),
    ('patch',    '1.2.3', '1.2.4'),

    # pre-base version
    ('premajor', '1.2.3', '2.0.0alpha1'),
    ('preminor', '1.2.3', '1.3.0alpha1'),
    ('prepatch', '1.2.3', '1.2.4alpha1'),

    # add pep specific parts
    ('pre',      '1.2.3', '1.2.3alpha1'), # pre will now append the first value in ('alpha', 'beta', 'rc')
    ('alpha',    '1.2.3', '1.2.3alpha1'),
    ('beta',     '1.2.3', '1.2.3beta1'),
    ('rc',       '1.2.3', '1.2.3rc1'),

    # update alpha -> beta -> rc
    ('beta',     '1.2.3alpha1', '1.2.3beta1'),
    ('rc',       '1.2.3beta1',  '1.2.3rc1'),

    # bump alpha, beta, rc
    ('alpha',    '1.2.3alpha1', '1.2.3alpha2'),
    ('pre',      '1.2.3alpha1', '1.2.3alpha2'),
    ('beta',     '1.2.3beta1',  '1.2.3beta2'),
    ('pre',      '1.2.3beta1',  '1.2.3beta2'),
    ('rc',       '1.2.3rc1',    '1.2.3rc2'),
    ('pre',      '1.2.3rc1',    '1.2.3rc2'),

    # add special part
    #('pre',      '1.2.3', '1.2.3rc1'), # disabled because of changes in bump_pre implementation
    ('post',     '1.2.3', '1.2.3.post1'),
    ('dev',      '1.2.3', '1.2.3.dev1'),
    ('local',    '1.2.3', '1.2.3+1'),

    # bump special part
    ('pre',      '1.2.3rc1', '1.2.3rc2'),
    ('post',     '1.2.3.post1', '1.2.3.post2'),
    ('dev',      '1.2.3.dev1', '1.2.3.dev2'),
    ('local',    '1.2.3+1', '1.2.3+2'),

    # release
    ('release', '1.2.3rc1', '1.2.3'),
    ('release', '1.2.3.post1', '1.2.3.post1'),
    ('release', '1.2.3.dev1', '1.2.3.dev1'),
    ('release', '1.2.3+1', '1.2.3'),

])
def test_bump_version(rule, old, new):
    assert bump_version(rule=rule, version=old, scheme='pep') == new, "Rule {} failed for '{}'!".format(rule, old)
