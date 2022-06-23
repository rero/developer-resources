# Imports

Python imports can be reorganized, sorted, and changed during development.

Here are some best practices about Python imports.

## Usage of absolute/relative imports

Python allows importing of resources using a path that is either absolute, or 
relative to current file. The guidelines for RERO-ILS project are defined as 
follows:
* Always give priority to absolute paths when importing 
  resources/classes/methods from outside the current module.
* Use relative path when importing resources/classes/methods of the same 
  module.

### example
into the file `rero_ils.modules.items.api.record.py`
```python
# These imports reference classes/methods from file into `items` module.
# As we stay into the same module, we use relative imports
from .api import ItemsSearch
from ..models import TypeOfItem
from ..utils import item_pid_to_object

# These imports reference classes/methods from file outside `items` module.
# Use absolute imports in this case (even if we stay into the RERO-ILS project
# scope)
from rero_ils.modules.api import IlsRecord
from rero_ils.modules.location.api import Location
from rero_ils.modules.operation_logs.extensions import UntrackedFieldsOperationLogObserverExtension
from rero_ils.modules.utils import date_string_to_utc, extracted_data_from_ref
```

## Sort imports

```bash
poetry run isort -rc rero_ils tests
```

## Remove unused imports

```bash
poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r .
```

## Tip: create an alias to sort imports and remove unused imports

Add a new line in your **.bashrc** or **.zshrc**:

```bash
alias fixsort="poetry run isort -rc rero_ils tests && poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r ."
```