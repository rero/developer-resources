# How to integrate UI in RERO-ils

## Latest version

To install latest version published on npm:

`cd path/to/invenio/instance/folder/static`

`npm install @rero/rero-ils-ui@latest`

## From a PR

### In RERO-ILS-UI

First:

```bash
git checkout rero/pr/xxx
npm install
npm run pack
```

Then copy rero-rero-ils-ui-0.0.x.tgz into RERO-ils directory.

### In RERO-ILS

And finally:

```bash
poetry run bootstrap -t path/to/rero-rero-ils-ui-0.0.x.tgz
```
