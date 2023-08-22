# Developer Resources

This documentation project serves as a starting point and reference for contributors of RERO+ projects. It summarizes technologies and modules used to develop and create an [Invenio application][1], and more specifically a [RERO ILS application][2].

Feel free to add:

* scripts and tools
* documentation about each technologies
* examples
* etc.

[1]: https://invenio.readthedocs.io
[2]: https://github.com/rero/rero-ils

## Circulation

* [`invenio-circulation` module](circulation/invenio-circulation.md)
* [RERO-ILS circulation module](circulation/circulation-module.md)

## Coding

* [Python](coding/python.md)
* [General recommendations](coding/recommendations.md): imports, typing, serialization, etc.
* [RERO ILS Debugging](coding/rero-ils-debug-specifics.md)
* [Editor configuration](coding/editor-configurations.md)

## Data

* [Data graph generation](data/data-graph-generation.md): generate graph to
  visualize data structure
* [Resource relations](data/resource-relations.md)

### Data model

* [Jsonschema](data/jsonschema.md): how to write a jsonschema for RERO+ apps
* [Checklist](data/data-model-checklist.md) for implementing a new field in the data model

### Database

All database stuff.

* [`invenio-db` module](data/invenio-db.md)
* [`invenio-pidstore` module](data/invenio-pidstore.md)
* [`invenio-records` module](data/invenio-records.md)
* [Sqlalchemy](data/sqlalchemy.md)
  * examples: [data/examples/](data/examples/)
* [PID reservation (CLI)](data/pid-reservation.md)
* [POST MARCXML via CURL and access token](data/post-marcxml-curl.md)

### Indexing

* [Elasticsearch](data/elasticsearch.md)
* [`invenio-indexer` module](data/invenio-indexer.md)
* [`invenio-records-rest` module](data/invenio-records-rest.md)
* [`invenio-search` module](data/invenio-search.md)

### Git & GitHub

* [git](git-github/git.md)
* [git workflow](git-github/workflow.md)
* [pull request creation](git-github/pull-rquests.md)
* [How to publish a release](rero-instances/release-publication.md)
* [How to generate a changelog](rero-instances/generate-changelog.md)

### Interface

* [invenio-assets](interface/invenio-assets.md)
* [invenio-theme](interface/invenio-theme.md)
* [invenio-records-ui](interface/invenio-records-ui.md)
* [invenio-search-ui](interface/invenio-search-ui.md)
* [nvm](interface/nvm.md)
* [layout charter](interface/layout-charter.md)
* [layout for document views (textual representation)](interface/layout-document-views.md)
* [Organisation views layout customization](interface/org-layout-customization.md)

### Invenio

* [invenio](invenio/invenio.md)
* [workshop1 (2016/12/21)](invenio/workshop1.md)

### Permissions

* [Permissions policy](permissions/policy.md)
* [invenio-user-management](permissions/invenio-user.md)
* [Generate access token](permissions/generate_oauth_token.md)

### [RERO projects and instances](rero-instances/README.md)

* [docker](rero-instances/docker.md)
* [poetry](rero-instances/poetry.md)
* [`russian_dolls`](https://github.com/rero/rero-ils/blob/staging/scripts/russian_dolls): to install `ng-core` in `rero-ils-ui` and `rero-ils-ui`
  in `rero-ils`.

#### [ng-core](rero-instances/README.md#ng-core)

* [How to check result from ng-core into RERO ILS](rero-instances/ng-core/ng-core-integration.md)

#### [RERO ILS](rero-instances/README.md#rero-ils)

* [Development environment installation](rero-instances/rero-ils/dev_installation.md)

#### [RERO ILS UI](rero-instances/README.md#rero-ils-ui)

* [Useful commands](rero-instances/useful-commands.md)
* [Migrate from a NodeJS version to another](interface/nvm.md#migration)
* [UI integration](rero-instances/rero-ils-ui/ui-integration.md): how to integrate UI in RERO-ILS

### Tests

* [pytest](tests/pytest.md)
* [cypress](tests/cypress.md)
* RERO ILS [data for tests](tests/data-for-tests.md)
* [Load testing](tests/load-testing/load-testing.md)

### [Translation](translations)

* [babel](translations/babel.md)
* [how to add a new language](translations/add-language.md)
* [Translations Workflow](translations/translations-workflow.md)
