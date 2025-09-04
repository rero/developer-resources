# Recommendations

Some coding recommendations specific to RERO+ projects.

## Python linting and formatting (ruff)

Since mid-2025, RERO+ projects use [ruff](https://docs.astral.sh/ruff/) to format Python files. Here is how to configure VSCode so that your code is always conform:

1. Install the [ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) extension
2. Go to VSCode Settings CTRL+Shift+P "Preferences: Open User Settings (JSON)"
3. Use these settings for python:

```json
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true,
        "editor.wordWrap": "off",
        "editor.rulers": [120],
        "editor.tabSize": 4,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
```

This will format and lint your Python code with ruff every time you save a python file. It will also add a vertical line at 120 characters.

Once the extension is installed and you have a .venv with ruff, the editor will inform you of any problems with the linter.

The rules used by `ruff` are defined in the `pyproject.toml` of each project under `[tool.ruff]`. For example, you can add any exceptions to the rules in the config.

To format the files in your project

```bash
uv run poe format
```

To check linting on the whole project:

```bash
uv run poe lint
```

## Python imports

Python imports can be reorganized, sorted, and changed during development. `ruff` will sort and clean your imports automatically.

Here are some best practices about Python imports.

### Usage of absolute/relative imports

Python allows importing of resources using a path that is either absolute, or relative to current file. The guidelines for RERO-ILS project are defined as follows:

* Always give priority to absolute paths when importing resources/classes/methods from outside the current module.
* Use relative path when importing resources/classes/methods of the same module.

#### Example

in the file `rero_ils.modules.items.api.record.py`

```python
# These imports reference classes/methods from the `items` module.
# As we stay into the same module, we use relative imports
from .api import ItemsSearch
from ..models import TypeOfItem
from ..utils import item_pid_to_object

# These imports reference classes/methods from outside the `items` module.
# Use absolute imports in this case (even if we stay in the RERO-ILS project
# scope)
from rero_ils.modules.api import IlsRecord
from rero_ils.modules.location.api import Location
from rero_ils.modules.operation_logs.extensions import UntrackedFieldsOperationLogObserverExtension
from rero_ils.modules.utils import date_string_to_utc, extracted_data_from_ref
```

## Python typing

Introduced since Python `3.5`, [typing](https://docs.python.org/fr/3.10/library/typing.html)
allows to specify types for variables or functions. For RERO+ projects, this
feature is not recommended, since it doesn't add any value to the code.

## Data serialization

Exporting long lists of results from an ES query implies using `scan()` instead
of `execute()`. `execute()` uses `invenio-record-rest` but not `scan()`. This
means that we have to duplicate code when using `scan()`.

* As of 2022-07, we keep using `invenio-record-rest`. When we need to stream an
export with `scan()`, we use a specific mounting point.
* Long-term, we can begin to migrate some resources to `Invenio resources`,
which is more flexible and allows class supercharging.
* To avoid high server loads, limit the number of results for each export with
a config variable. Above this limit, streaming is not allowed and requires an
external task.
* `scan()` can create ElasticSearch timeouts. Each export task should be
possible with a CLI that avoids any nginx or ES timeout.

## Angular/Typescript linting (eslint)

Our Angular projects use ESLint with a configuration file in the root of each project `eslint.config.js`

Configure your editor so that it shows you errors and warnings directly in the code:

1. Install the [eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) extension
2. Go to VSCode Settings CTRL+Shift+P "Preferences: Open User Settings (JSON)"
3. Use these settings:

```json
    "typescript.validate.enable": false,
    "css.lint.unknownAtRules": "ignore",
    "scss.lint.unknownAtRules": "ignore",
    "eslint.enable": true,
    "eslint.format.enable": true,
    "eslint.validate": ["javascript", "typescript", "html"],
    "eslint.useFlatConfig": true,
    "eslint.workingDirectories": ["../projects/**/src"],
    "eslint.options": {
        "overrideConfigFile": "eslint.config.js"
    },
    "[typescript]": {
        "editor.wordWrap": "off",
        "editor.formatOnSave": false,
        "editor.defaultFormatter": "dbaeumer.vscode-eslint",
        "editor.tabSize": 2,
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit"
        }
    },
```

## Prettyfier

Recommended code formatting/prettyfier plugins:

* Typescript/Angular: *to be determined*

**Note:** Cosmetic suggestions in code reviews should be identified as such, and
can be ignored by the author of the original code.
