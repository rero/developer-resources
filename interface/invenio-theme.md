# invenio-theme

Invenio standard theme. It is based on `Flask` and `jinja` templates and uses `invenio-assets`.

## Configurations

```python
HEADER_TEMPLATE = 'invenio_theme/header.html'
BASE_TEMPLATE = 'invenio_theme/page.html'
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
SETTINGS_TEMPLATE = 'invenio_theme/settings/content.html'

THEME_LOGO = 'images/simple_app_logo.png'
```

## Example: change the Footer

### 1. create new page and footer templates file in you `templates` directory

```bash
mkdir my_instance/templates/my_instance
touch my_instance/templates/my_instance/page.html
touch my_instance/templates/my_instance/footer.html
```

### 2. set the configuration to you new file

```python
BASE_TEMPLATE = 'my_instance/page.html'
```

### 3. collect static files

```bash
my_instance collect -v
```

### 4. set the content of the templates

page.html:

```html
<!-- inheritance -->
{% extends 'invenio_theme/page.html' %}

<!-- redefine footer -->
{%- block page_footer %}
    <!-- external file -->
    {% include 'simple_app/footer.html' %}
{%- endblock page_footer %}
```

footer.html

```html
<!-- footer block -->
<footer id="footer">
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12 col-md-12" style="text-align: right;">
        <hr />
        <ul class="list-unstyled">
        <!-- language selector if defined -->
          {% if config.I18N_LANGUAGES %}
            {% from "invenio_i18n/macros/language_selector.html" import language_selector %}
            <li>
              {{ language_selector() }}
            </li>
          {% endif %}
          <!-- replace Invenio link by RERO -->
          <li>
            {% trans link="http://www.rero.ch" %}Powered by <a href="{{link}}">RERO</a>{% endtrans %}
          </li>
        </ul>
      </div>
    </div>
  </div>
</footer>
```

## References

1. [Official Documentation](https://invenio-theme.readthedocs.io)
