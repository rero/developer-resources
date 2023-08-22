# invenio-records-rest

## API

REST API for invenio-records.

### Usage of the REST API

The base url for the REST is `/api` and is hardcoded in the `factory.py` file.

```bash
# search
curl -X GET "http://localhost:5000/api/records/?q=John"

# get one record
curl -X GET http://localhost:5000/api/records/5

# delete
curl -X DELETE http://localhost:5000/api/records/5

# update
curl -X PUT -H "Content-Type: application/json" -d'{"$schema": "http://simple_app.rero.ch/schemas/records/records-v0.0.1.json", "author": "me", "category": "perl", "control_number": "5", "description": "bla", "status": "beta", "title": "mon titre"}' http://localhost:5000/api/records/5

# create
curl -X POST -H "Content-Type: application/json" -d'{"$schema": "http://simple_app.rero.ch/schemas/records/records-v0.0.1.json", "author": "me", "category": "perl", "description": "bla", "status": "beta", "title": "mon titre"}' http://localhost:5000/api/records/

# patch
curl -X PATCH -H "Content-Type: application/json-patch+json" -d'[{"op": "replace", "path": "/title", "value": "mon titre"}]' http://localhost:5000/api/records/5

# get options
curl -X GET "http://localhost:5000/api/records/_options"

# get suggester
curl -X GET "http://localhost:5000/api/records/_suggest?title=queit&author=jonh"
```

### Configuration

Theses configurations should be defined in the `config.py` file of the Invenio instance.

#### Rest endpoints

```python
RECORDS_REST_ENDPOINTS = dict(
    recid=dict(

        ## Required

        # persistant id type
        pid_type='recid',

        # url for one record
        list_route='/records/',

        # to format one record for exportation, can content a list
        # of mimes for content negociation
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response')
        },

        # url for list of records pid() convert recid to UUID
        item_route='/records/<pid(recid, record_class="invenio_records_rest.memento.MementoRecord"):pid_value>',

        # to format one record for exportation
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search')
        },

        ## Optional

        # needed as REST allow record creation
        pid_minter='recid',
        pid_fetcher='recid',

        # for record creation
        #record_class='invenio_records.api.Record',
        record_class='invenio_records_rest.memento.MementoRecord',

        # for record creation and update
        record_loaders={
            'application/json': lambda: request.get_json(),
            'application/json-patch+json': lambda: request.get_json(force=True)
        },

        # permissions
        read_permission_factory_imp=allow_all,
        create_permission_factory_imp=check_admin,
        delete_permission_factory_imp=check_admin,
        update_permission_factory_imp=check_admin,

        # search preferences
        # can be indexes or alias: records or records-records-v0.0.1
        # search_index='records-records-v0.0.1',
        search_index='records',
        search_type=['records-v0.0.1'],

        # default mime type for content negiciation
        default_media_type='application/json',

        # for multiple endpoints for a given pid_type
        # will change links endpoints
        default_endpoint_prefix=True,

        # create a /records/_options to list options
        use_options_view=True,

        # factory to create next, prev, properties in the json object
        links_factory_imp=('invenio_records_rest.links:'
                              'default_links_factory'),

        # elasticsearch suggesters, for example:
        # /records/_suggest?author=jonh smiht&title=queit
        suggesters=dict(
            author=dict(
                term=dict(field='author')
            ),
            title=dict(
                term=dict(field='title')
            ),
        ),

        # max returned results
        max_result_window=10000
    )
)
```

Sample of authentication function. It allow admin action for logged admin users and requests comming from `localhost`.

```python
def check_admin(record, *args, **kwargs):
    def can(self):
        print(request)
        if request.remote_addr == '127.0.0.1':
            return True
        return DynamicPermission(ActionNeed('admin-access'))
    return type('CheckIp', (), {'can': can})()
```

#### Facets

```python
RECORDS_REST_FACETS = dict(
    records=dict(
        aggs=dict(
            status=dict(terms=dict(field='facet_status')),
            category=dict(terms=dict(field='facet_category')),
            author=dict(terms=dict(field='facet_author'))
        ),

        # can be also post_filter
        filters=dict(
            status=terms_filter('facet_status'),
            category=terms_filter('facet_category'),
            author=terms_filter('facet_author')

        )
    )
)
```

#### Sorting

```python
RECORDS_REST_SORT_OPTIONS = dict(
    records=dict(
        bestmatch=dict(
            fields=['-_score'],
            title='Best match',
            default_order='asc',
            order=1,
        ),
        mostrecent=dict(
            fields=['-_created'],
            title='Most recent',
            default_order='asc',
            order=2,
        )
    )
)

#: Default sort for records REST API.
RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(query='bestmatch', noquery='mostrecent'),
)
```

## References

1. [Official Documentation](http://pythonhosted.org/invenio-records-rest)
