#invenio-search-ui

UI for Invenio-Search. It uses `invenio-search-js` an angular application.


## Installation

```python
pip install ...
```
You need to install `javascript` dependencies and assets. This is usually done during the instance installation (`scripts/populate.sh):

```bash
# update the packages.json for js dependencies
my_instance npm
cdvirtualenv var/my_instance-instance/static

# install js dependencies
npm install

# collect static files
my_instance collect -v

# compile css and javascript
my_instance assets build
```
### Important Note

As we use `angular` templates we need to disable cache in the browser for the template update:

## Basic configuration

This will change the summary view in the `angularjs` `invenio-search` application.
```python
SEARCH_UI_JSTEMPLATE_RESULTS = 'templates/my_instance/brief.html'
```

### Example of Record Brief Template

```html
<ul>
  <!-- Records iterators -->
  <li ng-repeat="record in vm.invenioSearchResults.hits.hits track by $index">
    <!-- FIXME find a better way to set the record url -->
    <h4><a target="_self" ng-href="/records/{{ record.id }}">{{ record.metadata.title }}</a></h4>
    <!-- Summary -->
    <p>{{ record.metadata.description }}</p>
    <!-- Links -->
    <div class="text-right">
      <ul class="list-inline">
        <li ng-show="record.metadata.author">
          <a ng-click="showAuthors=!showAuthors">
            {{ showAuthors ? 'Hide authors' : 'Show authors' }}
          </a>
        </li>
        <li>
          <a ng-click="showSource=!showSource">
            {{ showSource ? 'Hide source' : 'Show source' }}
          </a>
        </li>
      </ul>
    </div>
    <!-- Authors list -->
    <div ng-hide="!showAuthors">
      <ul>
        <div>
          <li>{{ record.metadata.author }}</li>
        </div>
      </ul>
    </div>
    <!-- Original record source -->
    <div ng-hide="!showSource">
      <pre>{{ record | json }}</pre>
    </div>
    <hr />
  </li>
</ul>
```


## Other Configurations

```python
SEARCH_UI_SEARCH_API = '/api/records/'
"""Configure the search engine endpoint."""

SEARCH_UI_SEARCH_INDEX = 'records'
"""Name of the search index used."""

SEARCH_UI_SEARCH_TEMPLATE = 'invenio_search_ui/search.html'
"""Configure the search page template."""

SEARCH_UI_JSTEMPLATE_COUNT = 'templates/invenio_search_ui/count.html'
"""Configure the count template."""

SEARCH_UI_JSTEMPLATE_ERROR = 'templates/invenio_search_ui/error.html'
"""Configure the error page template."""

SEARCH_UI_JSTEMPLATE_FACETS = \
    'node_modules/invenio-search-js/dist/templates/facets.html'
"""Configure the facets template."""

SEARCH_UI_JSTEMPLATE_RANGE = 'templates/invenio_search_ui/range.html'
"""Configure the range template."""

SEARCH_UI_JSTEMPLATE_RANGE_OPTIONS = {'histogramId': '#year_hist',
                                      'selectionId': '#year_select',
                                      'name': 'years',
                                      'width': 180}
"""Configure the range template options."""

SEARCH_UI_JSTEMPLATE_LOADING = 'templates/invenio_search_ui/loading.html'
"""Configure the loading template."""

SEARCH_UI_JSTEMPLATE_PAGINATION = 'templates/invenio_search_ui/pagination.html'
"""Configure the pagination template."""

SEARCH_UI_JSTEMPLATE_SELECT_BOX = 'templates/invenio_search_ui/selectbox.html'
"""Configure the select box template."""

SEARCH_UI_JSTEMPLATE_SORT_ORDER = \
    'templates/invenio_search_ui/togglebutton.html'
"""Configure the toggle button template."""
```

## References

1. [Official Documentation](https://invenio-search-ui.readthedocs.io)