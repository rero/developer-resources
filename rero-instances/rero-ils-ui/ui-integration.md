# How to integrate UI in RERO-ils

## From NPM latest published version

If you want to use the last NPM published version, do:

```bash
cd path/to/invenio/instance/folder/static
npm install @rero/rero-ils-ui@latest
```

## From a PR

This should be done in several steps.

First, in rero-ils-ui:

```bash
cd path/to/rero-ils-ui
git checkout rero/pr/xxx
npm install
npm run pack
```

Then use **bootstrap script** with this new file:

```bash
cd path/to/rero-ils
poetry run bootstrap -t ../rero-ils-ui/rero-rero-ils-ui-0.0.x.tgz
```
