# Babel

[Babel](http://babel.pocoo.org/) includes a command-line interface for working with message catalogs, similar to the various GNU gettext tools commonly available on Linux/Unix systems.

## Usage

Even if `babel` provide command line interface it is usually easy to use: `setup.py` commands:

- **create a new language**: `setup.py init_catalog -f <lang>`
- **extract new texts to translate**: `setup.py extract_messages`
- **extract update languge files to translate**: `setup.py update_catalog`
- **make translation available for the system**: `setup.py compile_catalog`

## Transifex

[Transifex](https://www.transifex.com) is a centralize plateform for translations. An RERO [project](https://www.transifex.com/rero) exists.