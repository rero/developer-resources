# How to check result from ng-core into RERO ILS

When developing on ng-core, you sometimes want to check the result in RERO ILS.

As RERO ILS (rero-ils) uses RERO ILS UI (rero-ils-ui) and RERO ILS UI uses ng-core, you need to follow a specific procedure:

```bash
cd ng-core
npm ci && npm run pack  # this generates i.e. rero-ng-core-0.7.0.tgz file
cd -
cd rero-ils-ui
npm ci && \
    npm i ../ng-core/rero-ng-core-0.x.0.tgz && \
    npm run pack  # this generates i.e rero-rero-ils-ui-0.4.0.tgz file
```

Now you get a rero-ils-ui package file you need to include it in rero-ils. For that you have 2 solutions:

1. Use bootstrap command in rero-ils (easy, but takes several minutes).
2. Integrate directly the rero-ils-ui package into the static directory (more complicated but less than minute).

## Method 1: use bootstrap

Just do:

```bash
cd rero-ils
poetry run bootstrap -t ../rero-ils-ui/rero-rero-ils-ui-0.y.0.tgz
```

## Method 2: integrate it directly to static directory

In short, it could be:

```bash
cd rero-ils
npm i ../rero-ils-ui/rero-rero-ils-ui-0.y.0.tgz --prefix "$(poetry run invenio shell --no-term-title -c "print('static_folder:%s' % app.static_folder)"|grep static_folder| cut -d: -f2-)" && poetry run invenio assets build
```

And more understandable:

```bash
cd rero-ils
cd ../var/ils/static
npm i ../../../rero-ils-ui/rero-rero-ils-ui-0.y.0.tgz
cd -
poetry run invenio assets build
```