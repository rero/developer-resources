# inveno-assets

Media assets management for Invenio.

This module is based on `Flask-Assets` and `Flask-Collect`. It adds `nodejs` support and static files `invenio` modules collection.


## Static Files Collection

In your module or `invenio` instance you have templates or static files such as images, etc. The `collect` command will go through all `invenio` install modules and make symlinks in the `Flask` `instance_dir` directory. This directory is to put generated files such as generated assets.

### Command Line Interface

```bash
my_instance collect -v      # collect static files from modules
```


## CSS and Javascript

This module is able to use `scss` and `requirejs` (use of nodejs in the frontend).

### NodeJS

Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Usually used in the backend it is possible to use it to the frontend using special filters.

### Entrypoints

```python
# setup.py
setup(
    entry_points={
        'invenio_assets.bundles': [
            'mycssbundle = my_instance.bundles:mycssbundle',
            'myjsbundle = my_instance.bundles:myjsbundle'
        ]
    }
)
 ```

### Assets

```python
from invenio_assets import NpmBundle
mycssbundle = NpmBundle(
    filters='scss, cleancss',
    output='mycssbundle.css',
    npm={
        'almond': '~0.3.1',
        'bootstrap-sass': '~3.3.5',
        'font-awesome': '~4.4.0',
    }
)
```

### Using it in Templates

```html
{% assets "mycssbundle" %}<link href="{{ ASSET_URL }}" rel="stylesheet">{% endassets %}
{% assets "myjsbundle" %}<script src="{{ ASSET_URL }}"></script>{% endassets %}

```

### Command Line Interface

```bash
my_instance npm             # create the list of nodejs module to install
                            # it will create a packages.json file in the instance_dir/static
                            # go to this dir and run 'npm install' to install js packages

my_instance assets build    # compile css and js this will create files in the
                            # instance_dir/static/gen directory
```


## References

1. [Official Documentation](https://invenio-assets.readthedocs.io)