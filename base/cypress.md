# Cypress

Cypress is a next generation front end testing tool built for the modern web. Complete documentation can be found [here](https://docs.cypress.io/guides/overview/why-cypress.html#In-a-nutshell).

This tool is integrated to RERO-ILS and the following documentation explains how to use it.

## Prerequisites

* `poetry run bootstrap`
* `poetry run setup`
* `poetry run server`

Local server (localhost:5000) must be running and the database must contain data, as Cypress will use them to run the tests.

## Configuration

`poetry run cypress` will install Cypress if it's not present and launch the tests in command line.

## Run the tests

The tests can be ran on command line or with a graphic test launcher. The second option allows to see the tests running, see the snapshots for each step and launch them individually.

### Command line

`poetry run cypress`

A video of the tests is created in folder **tests/e2e/cypress/cypress/videos**.

To run a single test:

* `cd tests/e2e/cypress/`
* `npx cypress run --spec "path/to/file.spec.js"`

The path should be relative to cypress folder, for example: **./cypress/integration/circulation/checkout-checkin.spec.js**

### With the test runner

* `cd tests/e2e/cypress`
* `npm run cypress` to open Cypress
* Run the test by clicking on corresponding `*.spec.js` file

The test runner is described in details [here](https://docs.cypress.io/guides/core-concepts/test-runner.html#Overview).

## Writing the tests

### File organisation

#### Base url

The base url is stored in cypress.json file, as recommended in the [best practices](https://docs.cypress.io/guides/references/best-practices.html#Setting-a-global-baseUrl).

#### Custom commands

In order to have re-usable code, some custom commands can be written here: **tests/e2e/cypress/cypress/support/commands.js**

For more informations, read the corresponding documentation [here](https://docs.cypress.io/api/cypress-api/custom-commands.html#Syntax).

### Selecting DOM elements

The [selector playground](https://docs.cypress.io/guides/core-concepts/test-runner.html#Selector-Playground) may be useful to select elements in DOM.

In countrary to what is said in [best practices](https://docs.cypress.io/guides/references/best-practices.html#Selecting-Elements), the context of RERO-ILS projects asks not to use specific attributes for DOM element selecting. Here is a list of selector we should use:


| Selectors | Example | Usage |
| --- | --- | ---|
| Id  | `cy.get('#main').click()` | Better |
| Name  | `cy.get('[name=submission]').click()` | Better |
| Text  | `cy.contains('Submit').click()` | Depends on translations |
| Specific attribute | `cy.get('[data-cy=submit]').click()` | To use only if there is no other way |

### Assertions

A list of assertions is available [here](https://docs.cypress.io/guides/references/assertions.html#BDD-Assertions).