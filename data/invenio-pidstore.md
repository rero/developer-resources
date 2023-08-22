# invenio-pidstore

Invenio module that stores and registers persistent identifiers.

## Command Line Interface

``` bash
my_instance pid --help        # usage
```

## Concepts

- `PersistentIdentifier`: for working with persistent identifiers ( create, reserve, register, delete, and redirect). It contains:
  - `pid_type`: persistent identifier schema (i.e. doi)
  - `pid_value`: persistent identifier (i.e. 10.1234/foo)
  - `object_type`: object type (i.e. rec for record).
  - `object_uuid`: object id
  - `status`: status of persistent identifier:
    - `NEW`: PID has *not* yet been registered with the service provider
    - `RESERVED`: PID reserved in the service provider but not yet fully registered
    - `REGISTERED`: PID has been registered with the service provider
    - `REDIRECTED`: PID has been redirected to another persistent identifier
    - `DELETED`: PID has been deleted/inactivated with the service provider
- `Resolver`: given a persistent identifier retrieve the assigned internal object. Only object with `REGISTERD` status is returned without exception.
- `Providers`: wrappers around a persistent identifier to provide extra functionality (e.g. interaction with remote services). Usually used by minters.
- `Minters`: small functions that are responsible for minting a specific persistent identifier type for a specific internal object type in as automatic way as possible.
- `Fetchers`: small functions that are responsible for returning a minted persistent identifier.

## API

### Packages Imports

```python
from invenio_pidstore.models import PersistentIdentifier, \
                                    PIDStatus, \
                                    PIDDoesNotExistError
from invenio_pidstore.resolver import Resolver
from invenio_pidstore import current_pidstore
from invenio_pidstore.providers.recordid import RecordIdProvider
from invenio_pidstore.errors import PIDAlreadyExists
```

### PersistentIdentifier

Most of the time pids are managed with minters.

```python

pid = PersistentIdentifier.create('doi', '10.1234/foo')  # create a new pid

assert pid.is_new()                                      # new status by default
assert pid.has_object() == False                         # no object assigned

# bug: will be solved in 1.0.0
# already exists thus pid creation will failed
# try:
#     pid = PersistentIdentifier.create('doi', '10.1234/foo')
# except:
#     pass

pid.delete()                                             # a pid with NEW status
                                                         # will be completely deleted from the DB
try:
    pid = pid.get('doi', '10.1234/foo')                  # as it is removed from the DB
except PIDDoesNotExistError:                             # it can not be retrieved
    pass

pid = PersistentIdentifier.create('doi', '10.1234/foo')  # creation again
pid.reserve()                                            # pid reservation for future uses
assert pid.is_reserved()                                 # check
assert pid.has_object() == False                         # no object assigned

rec = Record.create({'title': 'New Record with PID'})    # create a new record
pid.assign('rec', rec.id)                                # assign the record to the pid
pid.register()                                           # make it registered
assert pid.has_object()                                  # object assigned

assert pid.is_registered()                               # is registered

pid.delete()                                             # mark as removed as the status is not NEW
pid = pid.get('doi', '10.1234/foo')                      # pid exists in DB
assert pid.is_deleted()                                  # is deleted

pid = PersistentIdentifier.create(pid_type='recid',      # one line creation
                                  pid_value='1',
                                  object_type='rec',
                                  object_uuid=rec.id,
                                  status=PIDStatus.REGISTERED)

new_pid = PersistentIdentifier.create(pid_type='recid',  # a second one
                                      pid_value='2',
                                      object_type='rec',
                                      object_uuid=rec.id,
                                      status=PIDStatus.REGISTERED)

pid.redirect(new_pid)                                    # pid redirection pid -> new_pid
assert pid.is_redirected()                               # is redirected
assert new_pid == pid.get_redirect()                     # get redirected pid

db.session.commit()                                      # flush the transaction
```

### Resolver

```python
resolver = Resolver(pid_type='recid',                    # resolver creation
                    object_type='rec',
                    getter=Record.get_record)
pid, rec = resolver.resolve('1')                         # retrieve the object
existing_uuid = [rec_meta.id for rec_meta in RecordMetadata.query.all()]
assert rec.id in existing_uuid
```

### Providers

Most of the time pids are managed with minters.

```python
rec = Record.create({'title': 'New Record with PID'})    # create a record
db.session.commit()                                      # flush the transaction

# create a pid for a given record, recid will be incremented
provider = RecordIdProvider.create(object_type='rec', object_uuid=rec.id)
db.session.commit()

pid = RecordIdProvider.get(pid_value='1').pid            # get the pid given a pid_value
assert rec.id == pid.object_uuid                         # check ids
```

__Note__: do not mix provider with manual pid assignment

### Minters

#### Create a Minter

```python
def recid_minter(record_uuid, data):

    assert 'recid' not in data
    provider = RecordIdProvider.create(
        object_type='rec', object_uuid=record_uuid)
    data['recid'] = provider.pid.pid_value
    return provider.pid
```

#### Minter Usage

```python
# minter registration (can be done using entrypoints)
current_pidstore.register_minter('rec_id', recid_minter)


recidminter = current_pidstore.minters['rec_id']         # retrieve a minter

rec = Record.create({'title': 'New Record with PID'})    # create a record
pid = recidminter(rec.id, rec)                           # use the minter to create pid
assert rec['recid'] == pid.pid_value                     # the pid value is stored in the record
rec.commit()                                             # record has been modified
db.session.commit()
```

### Fetcher

#### Create a Fetcher

```python
from invenio_pidstore.fetchers import FetchedPID
def recid_fetcher(record_uuid, data):
    return FetchedPID(
        provider=RecordIdProvider,
        pid_type=RecordIdProvider.pid_type,
        pid_value=str(data['recid'])
    )
```

#### Usage

```python
# registration (can be done using entrypoints)
current_pidstore.register_fetcher('rec_id', recid_fetcher)
recidfetcher = current_pidstore.fetchers['rec_id']       # retrieve the fetcher
rec = Record.get_record(RecordMetadata.query.first().id) # get a record
fetcher = recidfetcher(rec.id, rec)                      # retrieve the pid
assert fetcher.pid_value == rec['recid']                 # check
```

## References

1. [Official Documentation](http://pythonhosted.org/invenio-pidstore)
