# invenio-db

Database management for Invenio.

## Command Line Interface

```bash
invenio db --help    # usage

invenio db init      # db creation
invenio db create    # tables creation

invenio db drop      # remove tables
invenio db destroy   # db deletion

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

## Migration

RERO ILS and invenio use [Alembic](https://alembic.sqlalchemy.org/en/latest/) to manage data migration through sqlalchemy.

### Command Line Interface

```bash
invenio alembic --help    # usage

invenio alembic  branches   # Show branch points.
invenio alembic  current    # Show current revision.
invenio alembic  downgrade  # Run downgrade migrations.
invenio alembic  heads      # Show latest revisions.
invenio alembic  log        # Show revision log.
invenio alembic  merge      # Create merge revision.
invenio alembic  mkdir      # Make migration directory.
invenio alembic  revision   # Create new migration.
invenio alembic  show       # Show the given revisions.
invenio alembic  stamp      # Set current revision.
invenio alembic  upgrade    # Run upgrade migrations.
```

### Entrypoints

```python
    'invenio_db.alembic': [
        'my_package = my_package.alembic'
    ],
```

### Create a new revision

```bash
invenio alembic revision 'my new revision'
```

This will basically create a new file in you `alembic` directory with existing
code with two functions `updgrade` and `downgrade`.

__Note:__ this can already contains auto generated migration code. It is
important to review it as the automatic generation is not perfect. For example
the table generation do not contains default values.

Here is a real example to migration some lines from on database to an other:

```python
# imports
from logging import getLogger

# alembic utils
from alembic import op
# local modules
from invenio_db import db
from invenio_records.models import RecordMetadata

from rero_ils.modules.collections.models import CollectionMetadata

# revision identifiers, used by Alembic.
revision = '9e3145d88e64'
# previous revision
down_revision = 'f0e7f3b80a21'
branch_labels = ()
depends_on = None

# to print messages
LOGGER = getLogger('alembic')
SCHEMA = 'https://bib.rero.ch/schemas/collections/collection-v0.0.1.json'


def upgrade():
    """Upgrade database."""
    # create the new table
    CollectionMetadata.metadata.create_all(bind=db.engine)
    # sanity check: the table should be empty
    assert CollectionMetadata.query.count() == 0
    # get all lines to migrate from the old table
    results = RecordMetadata.query.filter(
        RecordMetadata.json['$schema'].as_string() == SCHEMA).all()
    collections = [{
        'id': col.id,
        'json': col.json,
        'created': col.created,
        'updated': col.updated,
        'version_id': col.version_id
    } for col in results]
    # put the lines in the new table
    op.bulk_insert(CollectionMetadata.__table__, collections)
    # remove theses lines from the old table
    for col in results:
        db.session.delete(col)
    db.session.commit()
    LOGGER.info('migrate %s' % len(collections))


def downgrade():
    """Downgrade database."""
    # sanity check the old table do not contains the data
    assert RecordMetadata.query.filter(
        RecordMetadata.json['$schema'].as_string() == SCHEMA).count() == 0
    # get all lines from the new table
    results = CollectionMetadata.query.all()
    collections = [{
        'id': col.id,
        'json': col.json,
        'created': col.created,
        'updated': col.updated,
        'version_id': col.version_id
    } for col in results]
    # put back theses lines in the old table
    op.bulk_insert(RecordMetadata.__table__, collections)
    # need to close the session before removing the table
    db.session.close()
    # remove the new table
    op.drop_table('collection_metadata')
    LOGGER.info('migrate %s record collection' % len(collections))
```

### Tests

Imagine you need to test the revision `xxx+1`, use `invenio alembic stamp xxx` to force alembic to be one step before your revision, and run `invenio alembic upgrade` to test it. If the downgrade is well written, you can try `invenio alembic downgrade` to restore the data as before upgrade.

## References

1. [Official documentation](https://invenio-db.readthedocs.io/)
2. [Alembic for Invenio](https://invenio-db.readthedocs.io/en/latest/alembic.html)
3. [Flask-Alembic](https://flask-alembic.readthedocs.io/en/latest/)
4. [Alembic](https://alembic.sqlalchemy.org/en/latest/)
