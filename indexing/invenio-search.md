# invenio-search

Invenio module for information retrieval.

## API

## Command Line Interface

More usefull commands is defined in [invenio-indexer](indexing/invenio-indexer.md)

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
res = search \
        .query('query_string', query='title:*es*') \
        .filter('term', category='test')               # query + filter
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