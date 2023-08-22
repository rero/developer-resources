# invenio-search

Invenio module for information retrieval.

## Elasticsearch Mapping

In order to be able to index records at least one mapping file should exist. The directory name is the index name, the file name is the document type by default. Example: `simple_app/mappings/records/records-v0.0.1.json` will create an index name `records-records-v0.0.1` a document type `records-v0.0.1` and add `records-records-v0.0.1` to the `records` alias. This mapping must be declared in the `setup.py` file as:

```python
    'invenio_search.mappings': [
        'records = simple_app.mappings'
    ]
```

### Example of Mapping

```json
{
    "mappings": {
        "records-v0.0.1": {
            "date_detection": false,
            "numeric_detection" : false,
            "properties": {
                "$schema": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "_created": {
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                },
                "_updated": {
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                },
                "author": {
                    "type": "string",
                    "analyzer": "standard",
                    "copy_to": "facet_author"
                },
                "category": {
                    "type": "string",
                    "analyzer": "english",
                    "copy_to": "facet_category"
                },
                "control_number": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "description": {
                    "type": "string",
                    "analyzer": "english"
                },
                "status": {
                    "type": "string",
                    "index": "not_analyzed",
                    "copy_to": "facet_status"
                },
                "title": {
                    "type": "string",
                    "analyzer": "english"
                },
                "facet_author": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "facet_category": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "facet_status": {
                    "type": "string",
                    "index": "not_analyzed"
                }
            }
        }
    }
}
```

## API

## Command Line Interface

More useful commands are defined in [invenio-indexer](indexing/invenio-indexer.md)

```bash
my_instance index --help         # usage
```

### Import Package

```python
from invenio_search import RecordsSearch
from invenio_search import current_search
```

### Creation/Deletion

```python
from invenio_search import current_search
try:
    for index in current_search.delete():
        pass
    for index in current_search.create():
        pass
except:
    pass
assert 'records-records-v0.0.1' in current_search.mappings
```

### Record Indexing

See [invenio-indexer](indexing/invenio-indexer.md)

### Query

```python
from invenio_search import RecordsSearch

search = RecordsSearch()          # create search object
search = search.query('query_string', query='title:*Test*')
search = search.filter('term', category='test')               # query + filter
search.aggs.bucket('status', 'terms', field='status')  # facets
results = search.execute()                             # send the query to es
assert results.hits.total                              # number of results
assert results.hits.hits                               # list of results
assert results.aggregations.status.buckets             # facets
```

### Entrypoints

```python
    'invenio_search.mappings': [
        'records = simple_app.mappings'
    ]
```

## References

1. [Official Documentation](http://pythonhosted.org/invenio-search)
