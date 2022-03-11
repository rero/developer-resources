# Babel

[Babel](http://babel.pocoo.org/) includes a command-line interface for working with message catalogs, similar to the various GNU gettext tools commonly available on Linux/Unix systems.

## Usage

Even if `babel` provide command line interface it is usually easy to use: `setup.py` commands:

- **create a new language**: `setup.py init_catalog -f <lang>`
- **extract new texts to translate**: `setup.py extract_messages`
- **extract update languge files to translate**: `setup.py update_catalog`
- **make translation available for the system**: `setup.py compile_catalog`

## Weblate

[Weblate](https://hosted.weblate.org) is a centralized plateform for translations. A RERO [project](https://hosted.weblate.org/projects/rero_plus/) exists (see [translation workflow](translations-workflow.md)).
