## dephell_versioning

[![travis](https://travis-ci.org/dephell/dephell_versioning.svg?branch=master)](https://travis-ci.org/dephell/dephell_versioning)
[![appveyor](https://ci.appveyor.com/api/projects/status/github/dephell/dephell_versioning?svg=true)](https://ci.appveyor.com/project/orsinium/dephell-versioning)
[![MIT License](https://img.shields.io/pypi/l/dephell-versioning.svg)](https://github.com/dephell/dephell_versioning/blob/master/LICENSE)

Library for bumping project version.

Available schemes:

+ `calver`
+ `comver`
+ `pep`
+ `roman`
+ `romver`
+ `semver`
+ `serial`
+ `zerover`

Available rules (and aliases):

+ `init` -- initialize versioning
+ Main parts:
  + `major` (`breaking`)
  + `minor` (`feature`)
  + `patch` (`fix`, `micro`)
+ Additional parts:
  + `dev`
  + `local`
  + `post`
+ Pre-release management:
  + `pre` (`rc`, `alpha`, `beta`)
  + `premajor` (`prebreaking`)
  + `preminor` (`prefeature`)
  + `prepatch` (`prefix`, `premicro`)
  + `release`

Read more about schemes and rules in the documentation for [dephell project bump](https://dephell.readthedocs.io/en/latest/cmd-project-bump.html).

## Installation

install from [PyPI](https://pypi.org/project/dephell-versioning/):

```bash
python3 -m pip install --user dephell_versioning
```

## Usage

Get available schemes, rules, and aliases:

```python
from dephell_versioning import get_aliases, get_rules, get_schemes
get_schemes()
# frozenset({'roman', 'pep', ..., 'comver'})

get_rules()
# frozenset({'local', 'minor', ..., 'dev', 'preminor'})

get_aliases()
# frozenset({'alpha', 'rc', ..., 'micro', 'breaking'})
```

Bump version:

```python
from dephell_versioning import bump_version

bump_version(version='1.2.3', rule='minor', scheme='semver')
# '1.3.0'

# pass aliase instead of rule:
bump_version(version='1.2.3', rule='feature', scheme='semver')
# '1.3.0'

# start rule from `+` to attach local version number:
bump_version(version='1.2.3', rule='+456', scheme='semver')
# '1.2.3+456'

# for `init` version is optional
bump_version(version='', rule='init', scheme='semver')
# '0.1.0'
```

Bump version in a python file:

```python
from dephell_versioning import bump_file
from pathlib import Path

# returns `True` if version was bumped
bump_file(path=Path('dephell_versioning', '__init__.py'), old='0.1.0', new='0.1.1')
# True

# old version is optional: any version will be bumped if old isn't found
bump_file(path=Path('dephell_versioning', '__init__.py'), old='', new='0.1.2')
# True
```

Use [dephell_discover](https://github.com/dephell/dephell_discover) to find out the current version in a python project:

```python
from dephell_discover import Root
from pathlib import Path
root = Root(path=Path(), name='dephell_discover')

# root.metainfo can be None if project isn't found in the given directory
if root.metainfo:
    print(root.metainfo.version)
# '0.1.2'
```
