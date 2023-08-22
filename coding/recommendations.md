# Recommendations

Some coding recommendations specific to RERO+ projects.

## Python imports

Python imports can be reorganized, sorted, and changed during development.

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

### Sort imports

```bash
poetry run isort -rc rero_ils tests
```

### Remove unused imports

```bash
poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r .
```

### Tip: create an alias to sort imports and remove unused imports

Add a new line in your **.bashrc** or **.zshrc**:

```bash
alias fixsort="poetry run isort -rc rero_ils tests && poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r ."
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

## Prettyfier

Recommended code prettyfier plugins:

* Python: *to be determined*
* Typescript/Angular: *to be determined*

**Note:** Cosmetic suggestions in code reviews should be identified as such, and
can be ignored by the author of the original code.
