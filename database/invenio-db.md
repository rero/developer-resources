# invenio-db

Database management for Invenio.

## Command Line Interface

```bash
my_instance db --help    # usage

my_instance db init      # db creation
my_instance db create    # tables creation

my_instance db drop      # remove tables
my_instance db destroy   # db deletion

```

## API

### Creation

```python
# packages importation
from invenio_db import db
from sqlalchemy_utils.functions import create_database,\
                                       database_exists, drop_database

if database_exists(db.engine.url):
    drop_database(db.engine.url)        # remove if it exists
create_database(db.engine.url)          # create the db

db.drop_all()                           # remove tables
db.create_all()                         # create tables

# check if table exists
assert 'records_metadata' in db.metadata.tables

# db should be empty
from invenio_records.models import RecordMetadata
assert RecordMetadata.query.count() == 0
```

### Entrypoints
```python
    'invenio_db.models': [
        'my_records = my_package.models'
    ],
```

## Create a New Model (To Be Completed)

```python
from invenio_db import db

class MyModel(db.Model):
    """A new model.
    """

    __tablename__ = 'my_table_name'

    id = db.Column(
        UUIDType,
        primary_key=True,
        default=uuid.uuid4,
    )
    """Record identifier."""

    json = db.Column(
        JSONType().with_variant(
            postgresql.JSON(none_as_null=True),
            'postgresql',
        ),
        default=lambda: dict(),
        nullable=True
    )

```

## References

1. [Official documentation](http://pythonhosted.org/invenio-db)