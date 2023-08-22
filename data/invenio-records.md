# invenio-records

Invenio-Records is a metadata storage package.

## Command Line Interface

```bash
my_instance records --help       # usage

# create a simple record
echo "{'title': 'my title'}" | my_instance records create
```

## Concepts

Two classes exists for records:

- `RecordMetada`: this is the SQL model basically with the following columns:
  - `(UUIDType) id`: unique identifier
  - `(JSONType) json`: to store the data
  - `(Integer) version_id`: revision storage
  - `(DateTime) created`: creation date
  - `(DateTime) updated`: modification date
- `Record`: a wrapping class around `RecordMetadata`, this provide facilities such as data access, revisions, etc.

## API

### Python Packages

```python
from invenio_records.api import Record
from invenio_records.models import RecordMetadata
```

### Create a Record

```python
from invenio_db import db
from invenio_records.api import Record

rec = Record.create({'title': 'my title'}) # new Record
rec_uuid = rec.id                          # return UUID

assert rec.revision_id == 0                # first revision is 0

title = rec.get('title')                   # retrieve a value in json

assert title == 'my title'                 # check the value

db.session.commit()                        # terminate the transaction

db_rec = Record.get_record(rec_uuid)       # retrieve a Record

assert db_rec == rec                       # records should be equal
```

### Get Records

```python
from invenio_records.models import RecordMetadata
from invenio_records.api import Record

records = RecordMetadata.query.all()       # SQL query
for record in records:
    new_rec = Record.get_record(record.id) # create a Record instance
    assert new_rec.id == record.id         # Model id == instance id
```

### Update a Record

```python
from invenio_records.api import Record
from invenio_records.models import RecordMetadata

rec_uuid = RecordMetadata.query.first().id  # get the first db record
rec = Record.get_record(rec_uuid)           # create the record object
rec['title'] = 'new title'                  # change the title
db_rec = Record.get_record(rec_uuid)        # get the db version
assert db_rec != rec                        # not yet in db
rev_id_before_update = rec.revision_id      # store revision id
rec.commit()                                # push the changes
# new rev id
assert rec.revision_id == (rev_id_before_update + 1)
db.session.commit()                         # terminate the transaction
db_rec = Record.get_record(rec_uuid)        # get the db version
assert db_rec == rec                        # records are now equal
```

### Revisions

Invenio use the `SQLAlchemy` mecanism versioning provided by the `SQLAlchemy-Continuum` package.

```python
from invenio_records.api import Record
from invenio_records.models import RecordMetadata

rec_uuid = RecordMetadata.query.first().id  # get the first db record

# revision iterations
for rec in Record.get_record(rec_uuid).revisions:
    rev_id = rec.revision_id
    creation_date = rec.created
    modification_date = rec.updated
    record_data = rec.dumps()

rec = Record.get_record(rec_uuid)            # get the db record
rec = rec.revert(0)                          # revert to the first revision
db.session.commit()                          # terminate the transaction
```

### Validation with Json Schema

```python
from invenio_records.api import Record
from invenio_records.models import RecordMetadata
from jsonschema.exceptions import ValidationError

rec_uuid = RecordMetadata.query.first().id  # get the first db record
rec = Record.get_record(rec_uuid)           # create the record object
schema = {                                  # schema definition
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
    },
    'required': ['title']
}
rec = Record.get_record(rec_uuid)
rec.update({'$schema': schema})             # add schema to the record
rec.validate()                              # validation ok
rec['title'] = 3                            # put wrong value
try:                                        # exception should appears
    # validation is done during the commit
    rec.commit()                            # validation is done with commit
except ValidationError:
    pass

rec['title'] = 'validated title'            # correct value
rec.commit()                                # is valid
db.session.commit()                         # terminate the transaction
```

### Delete Records

```python
from invenio_records.api import Record
from invenio_records.models import RecordMetadata

records = RecordMetadata.query.all()        # fetch all records
for record in records:                      # for all records
    Record.get_record(record.id).delete()   # flag as deleted
    db.session.commit()                     # terminate the transaction 
    # remove from the db
    Record.get_record(record.id, with_deleted=True).delete(force=True)
    db.session.commit()                     # terminate the transaction 
```

### Signals

- before-record-insert
- after-record-insert
- before-record-update
- after-record-update
- before-record-delete
- after-record-delete
- before-record-revert
- after-record-revert

## References

1. [Official Documentation](http://pythonhosted.org/invenio-records)
