# invenio-indexer

Indexer for Invenio.

Invenio-Indexer is responsible for sending records for indexing in Elasticsearch so that the records can be searched. Invenio-Indexer can either send the records in bulk or individually. Bulk indexing is far superior in performance if multiple records needs to be indexed at the price of delay. Bulk indexing works by queuing records in a message queue, which is then consumed and sent to Elasticsearch.

## Command Line Interface

Some other commands is defined in [invenio-search](indexing/invenio-search.md)

```bash
my_instance index --help          # usage
my_instance index init            # create elasticsearch index and put mapping
my_instance index destroy         # remove all elasticsearch indexes
my_instance index queue init      # initialize indexing queue
my_instance index reindex         # push all records in the indexing queue
my_instance index run             # index records
```

## API

```python
from invenio_indexer.api import RecordIndexer
from invenio_records.api import Record

rec = Record.create({
        '$schema': 'http://simple_app.rero.ch/schemas/records/records-v0.0.1.json',
        'title': 'My Test',
        'description': 'bla',
        'author': 'me',
        'category': 'test',
        'status': 'draft',
        'control_number': 'test'
    })
RecordIndexer().bulk_index([rec.id])
RecordIndexer().process_bulk_queue()
```

### Signals

- before-record-index

## References

1. [Official Documentation](https://pythonhosted.org/invenio-indexer)
