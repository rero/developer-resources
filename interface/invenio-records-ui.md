# invenio-records-ui

## Configuration

```python
RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/records/<pid_value>',
        template='invenio_records_ui/detail.html'
    )
```

## Example: Title of the Detailed Page

Replace the recid as title to the real title of the document.

### 1. create a new template for the detailed view

```bash
touch my_instance/templates/my_instance/detail.html
```

Note: do not forget to run the static file collect: `my_instance collect -v`

### 2. set the `RECORDS_UI_ENDPOINTS.template` to the new file

```python
RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/records/<pid_value>',
        template='my_instance/detail.html'
    )

```

### 3. set the content of the file

```html
<!-- inheritance -->
{% extends 'invenio_records_ui/detail.html' %}

<!-- display title instead of recid -->
{%- block record_title %}
<h2>
  {{ record.title }}
</h2>
{%- endblock %}
```

## References

1. [Official Documentation](https://invenio-records-ui.readthedocs.io)
