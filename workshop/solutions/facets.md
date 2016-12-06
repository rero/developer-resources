# Navigation par facettes

## Rajouter la facette à l'interface

Remplacer les lignes suivantes dans `workshop/config.py`:

```python
RECORDS_REST_FACETS = dict(
    records=dict(
        aggs={
            'mime': dict(terms=dict(field='mime')),
            'genre': dict(terms=dict(field='genre', size=30)),
            'years': dict(date_histogram=dict(
                    field='year',
                    interval='year',
                    format='yyyy')
            )
        },
        filters=dict(
            mime=terms_filter('mime'),
            genre=terms_filter('genre')
        ),
        post_filters=dict(
            years=range_filter(
                'year',
                format='yyyy',
                end_date_math='/y'),
        )
    )
)
```

par:
```python
RECORDS_REST_FACETS = dict(
    records=dict(
        aggs={
            'artist': dict(terms=dict(field='facet_artist')),
            'mime': dict(terms=dict(field='mime')),
            'genre': dict(terms=dict(field='genre', size=30)),
            'years': dict(date_histogram=dict(
                    field='year',
                    interval='year',
                    format='yyyy')
            )
        },
        filters=dict(
            artist=terms_filter('artist'),
            mime=terms_filter('mime'),
            genre=terms_filter('genre')
        ),
        post_filters=dict(
            years=range_filter(
                'year',
                format='yyyy',
                end_date_math='/y'),
        )
    )
)
```

## Ajustement du mapping

La facette `artist` n'est pas correcte car on y voit de noms et prénoms. L'analyseur `Elasticsearch` doit être changé.

Remplacer les lignes suivantes dans ` workshop1/mappings/records/record-v1.0.0.json`:

```json
"artist": {
    "type": "string",
    "analyzer": "standard"
},
```

par:
```json
"artist": {
    "type": "string",
    "analyzer": "standard",
    "copy_to": "facet_artist"
},
"facet_artist": {
    "type": "string",
    "index": "not_analyzed"
},
```
Ne pas oublier de ré-indexer:

```bash
workshop1 index destroy --force
workshop1 index init
workshop1 index reindex
workshop1 index run
```
