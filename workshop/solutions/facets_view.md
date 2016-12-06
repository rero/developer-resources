## Ajustement la présentation de la facette

### Installation du fichier de template

```bash
mkdir -p workshop1/static/templates/workshop1
cp ../../var/workshop1-instance/static/node_modules/invenio-search-js/dist/templates/facets.html workshop1/static/templates/workshop1/.

workshop1 collect -v

echo "SEARCH_UI_JSTEMPLATE_FACETS = \
    'templates/workshop1/facets.html'" >> workshop1/config.py
```

### Modification du fichier de template

```html
...
<div ng-if="value.buckets.length > 0 && key !== 'years'" class="panel panel-default">
...
```