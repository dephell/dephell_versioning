from datetime import date

import pytest

from dephell_versioning._schemes import CalVerScheme


class PatchedCalVerScheme(CalVerScheme):
    @property
    def today(self):
        return date(2019, 8, 3)


@pytest.mark.parametrize('rule, old, new', [
    ('init', '', '2019.8'),
    ('major', '2019.1', '2019.8'),

    ('patch', '2019.1', '2019.8.3'),
    ('patch', '2019.8', '2019.8.3'),
    ('patch', '2019.8.1', '2019.8.3'),
    ('patch', '2019.8.12', '2019.8.13'),
])
def test_bump_version(rule, old, new):
    assert PatchedCalVerScheme().bump(rule=rule, version=old) == new
