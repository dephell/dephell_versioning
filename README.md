## dephell_versioning

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
