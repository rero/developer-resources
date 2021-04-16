# Developer Resources

This documentation will be a good starting point for RERO-ILS projects. This
will try to summary technologies and modules used to create an [Invenio
application][1], and more specifically a [RERO ILS application][2].

Feel free to add:

  * scripts and tools
  * documentation about each technologies
  * examples
  * etc.

[1]: https://invenio.readthedocs.io
[2]: https://github.com/rero/rero-ils

## Table of Content

### [Circulation](circulation/)

- [invenio-circulation module](circulation/invenio-circulation.md)
- [RERO-ILS circulation module](circulation/circulation-module.md)

### [Coding](coding/)

- [python](coding/python.md)
- [imports](coding/python-imports.md)
- python-debug (pdb)
- [RERO-ils specifics](coding/rero-ils-debug-specifics.md)
- [how to configure editors](coding/editor-configurations.md)

### [Data](data/README.md)

- [Data graph generation](data/data-graph-generation.md): generate graph to
  visualize data structure
- [Resource relations](data/resource-relations.md)

#### Data model

- [jsonschema](data/jsonschema.md)
- [guidelines on how to write a JSON schema](data/jsonschema.md#guidelines)
- [checklist](data-model-checklist.md) for implementing a new field in the
  data model


#### [Database](data/README.md#database)

All database stuffs.

- [invenio-db](data/invenio-db.md)
- [invenio-pidstore](data/invenio-pidstore.md)
- [invenio-records](data/invenio-records.md)
- [sqlalchemy](data/sqlalchemy.md)
    - examples: [data/examples/](data/examples/)
- [PID reservation (CLI)](data/pid-reservation.md)
- [POST MARCXML via CURL and access token](data/post-marcxml-curl.md)

#### [Indexing](data/README.md#indexing)

- [elasticsearch](data/elasticsearch.md)
- [invenio-indexer](data/invenio-indexer.md)
- [invenio-records-rest](data/invenio-records-rest.md)
- [invenio-search](data/invenio-search.md)

### [Documentation of the projects](documentation/README.md)

- [how to generate a changelog](documentation/generate-changelog.md)

### Git & GitHub

- [git](git-github/git.md)
- [git workflow](git-github/workflow.md)
- [pull request creation](git-github/pull-rquests.md)

### Interface

- [invenio-assets](interface/invenio-assets.md)
- [invenio-theme](interface/invenio-theme.md)
- [invenio-records-ui](interface/invenio-records-ui.md)
- [invenio-search-ui](interface/invenio-search-ui.md)
- [nvm](interface/nvm.md)
- [layout charter](interface/layout-charter.md)
- [layout for document views (textual
  representation)](interface/layout-document-views.md)
- [Organisation views layout
  customization](interface/org-layout-customization.md)

### Invenio

- [invenio](invenio/invenio.md)
- [workshop1 (2016/12/21)](invenio/workshop1.md)

### Lexicon

- [Lexicon](lexicon/lexicon.md)

### Permissions

- [invenio-user-management](permissions/invenio-user.md)
- [Generate access token](permissions/generate_oauth_token.md)

### [RERO projects and instances](rero-instances/README.md)

- pyenv
- [docker](rero-instances/docker.md)
- [poetry](rero-instances/poetry.md)
- [How to publish a release](rero-instances/release-publication.md)
- [`russian_dolls`][1]: to install `ng-core` in `rero-ils-ui` and `rero-ils-ui`
  in `rero-ils`.

[1]: https://github.com/rero/rero-ils/blob/dev/scripts/russian_dolls

#### [ng-core](rero-instances/README.md#ng-core)

- [How to check result from ng-core into RERO ILS](rero-instances/ng-core/ng-core-integration.md)

#### [RERO ILS](rero-instances/README.md#rero-ils)

- [Development environment installation](rero-instances/rero-ils/dev_installation.md)

#### [RERO ILS UI](rero-instances/README.md#rero-ils-ui)

- [Useful commands](rero-instances/useful-commands.md)
- [Migrate from a NodeJS version to another](interface/nvm.md#migration)
- [UI integration](rero-instances/rero-ils-ui/ui-integration.md):
  how to integrate UI in RERO-ILS

### Tests

- [pytest](tests/pytest.md)
- [cypress](tests/cypress.md)
- RERO ILS [data for tests](tests/data-for-tests.md)
- [Load testing](tests/load-testing/load-testing.md)

### [Translation](translation/README.md)

- [babel](translations/babel.md)
- [how to add a new language](translation/add-language.md)
