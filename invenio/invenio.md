# Invenio

## Installation

### Developpement

#### Create a Module

```bash
mkvirtualenv {MODULENAME}
cdvirtualenv
mkdir src
cd src/
git clone https://github.com/inveniosoftware/cookiecutter-invenio-module.git
pip install cookiecutter
cookiecutter cookiecutter-invenio-module
```

Example output with responses:

```bash
project_name [Invenio-FunGenerator]: Reroils-Record-Editor
project_shortname [reroils-record-editor]:
package_name [reroils_record_editor]:
github_repo [inveniosoftware/reroils-record-editor]:
description [Invenio module that adds more fun to the platform]: reroils record editor
author_name [CERN]: RERO
author_email [info@inveniosoftware.org]: software@rero.ch
year [2017]:
copyright_holder [RERO]:
copyright_by_intergovernmental [True]:
superproject [Invenio]:
transifex_project [reroils-record-editor]:
extension_class [ReroilsRecordEditor]:
config_prefix [REROILS_RECORD_EDITOR]:
```

```bash
cd {MODULENAME}

pip install sphinx
python setup.py test
pip install -e .

sphinx-build -qnNW docs docs/_build/html
```

Create repository on gitlab.rero.ch and push created module to it.
> Hidden files must be added to (Example: .editorconfig)

#### Create an Instance

### Production

## Technologies

## Modules

## Concepts

### Minter

### Fetcher

### Signals

### UUID
