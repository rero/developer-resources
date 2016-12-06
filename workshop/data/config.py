# -*- coding: utf-8 -*-

"""workshop1 base Invenio configuration."""

from __future__ import absolute_import, print_function
from invenio_records_rest.query import es_search_factory
from invenio_records_rest.facets import terms_filter, range_filter
from invenio_search import RecordsSearch

# Identity function for string extraction
def _(x):
    return x

# Default language and timezone
BABEL_DEFAULT_LANGUAGE = 'en'
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
I18N_LANGUAGES = [
]

HEADER_TEMPLATE = 'invenio_theme/header.html'
BASE_TEMPLATE = 'invenio_theme/page.html'
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
SETTINGS_TEMPLATE = 'invenio_theme/settings/content.html'

# WARNING: Do not share the secret key - especially do not commit it to
# version control.
SECRET_KEY = 'DQqrKwJkhMZaeHlwfF4aPlN4XWBQw0SdroXcq2E7HzWyFmCGEQbf99xJnrOAh4EskBTnTLTaay2o8vVnBAsO2LftzzQKE8nahmZaCVGdahLqhkMxhqJsvQFKpC2UIpiakof2QuirvVzSmsOSBeTwfMylz6iTkHGa6mhejsLFYvqKqqwLFVFo7NWWKugwzEuq2H1bds2AdHFouex8yskr4gsDIn795Zx1cWx7FygvM82THoRHeuGY7rBYVXv5MURb'

# Theme
THEME_SITENAME = _('workshop1')
THEME_LOGO='images/logo.png'
SEARCH_UI_JSTEMPLATE_FACETS = 'templates/workshop1/facets.html'
SEARCH_UI_JSTEMPLATE_RESULTS = 'templates/workshop1/record_brief.html'
SEARCH_UI_JSTEMPLATE_RANGE = 'node_modules/invenio-search-js/dist/templates/range.html'

# invenio-jsonschemas
JSONSCHEMAS_HOST = 'workshop.rero.ch'

# invenio-records-rest
RECORDS_REST_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        search_class=RecordsSearch,
        search_index='records',
        search_type=None,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        search_factory_imp= es_search_factory,
        list_route='/records/',
        item_route='/records/<pid(recid):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
    ),
)

# sort
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
        ),
        album=dict(
            fields=['sort_album'],
            title='Album',
            default_order='asc',
            order=3,
        ),
        artist=dict(
            fields=['facet_artist'],
            title='Artist',
            default_order='asc',
            order=4,
        )
    )
)

RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(query='bestmatch', noquery='album'),
)

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
            artist=terms_filter('facet_artist'),
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
