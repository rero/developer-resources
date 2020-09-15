# Cypress

Cypress is a next generation front end testing tool built for the modern web. Complete documentation can be found [here](https://docs.cypress.io/guides/overview/why-cypress.html#In-a-nutshell).

This tool is integrated to RERO-ILS and the following documentation explains how to use it.

## Prerequisites

* `poetry run bootstrap`
* `poetry run setup`
* `FLASK_DEBUG=False poetry run server`

Local server (localhost:5000) must be running and the database must contain data, as Cypress will use them to run the tests.
Note that setting `FLASK_DEBUG` to false means that the server should be restarted to take changes into account.

## Quick installation

`poetry run cypress` will install Cypress if not present. Then launch tests in command line.

## Setup your IDE

[A dedicated page about IDE](https://docs.cypress.io/guides/tooling/IDE-integration.html) explains:

* how to setup your IDE
* which extensions to use

For example, **to recognize files in your IDE** you can add this line in the head of each file:

```javascript
/// <reference types="Cypress" />
```

**The best way to work on cypress directory with VSCode is to consider `tests/e2e/cypress` as a project directory.** So launch VSCode in `tests/e2e/cypress` directory.

## Run the tests

The tests can be ran on command line or with a graphic test launcher. The second option allows to see the tests running, see the snapshots for each step and launch them individually.

### Command line

`poetry run cypress`

A video of the tests is created in folder **tests/e2e/cypress/cypress/videos**.

To run a single test:

* `cd tests/e2e/cypress/`
* `npx cypress run --spec "path/to/file.spec.js"`

The path should be relative to cypress folder, for example: **./cypress/integration/circulation/checkout-checkin.spec.js**

### With a GUI (the test runner)

* `cd tests/e2e/cypress`
* `npm run cypress` to open Cypress
* Run the test by clicking on corresponding `*.spec.js` file

The test runner is described in details [here](https://docs.cypress.io/guides/core-concepts/test-runner.html#Overview).

## Writing the tests

### File organisation

#### Configuration

The configuration of cypress is set in cypress.json file. The current settings are:
* The base url, as recommended in the [best practices](https://docs.cypress.io/guides/references/best-practices.html#Setting-a-global-baseUrl)
* The default command timeout
* The response timeout (for API url)
* The height and width of viewport (preview of the test)

#### Custom commands

In order to have re-usable code, some custom commands are listed here: **tests/e2e/cypress/cypress/support**. They are sorted by type:
* circulation.js
* navigation.js
* record.js
* user.js
* utils.js

All these files must be declared in index.js to be able to use the commands in the project.
For more informations, read the corresponding documentation [here](https://docs.cypress.io/api/cypress-api/custom-commands.html#Syntax).

### Selecting DOM elements

The [selector playground](https://docs.cypress.io/guides/core-concepts/test-runner.html#Selector-Playground) may be useful to select elements in DOM.

**Warning**: Selector Playground seems not to be working on Chromium 83.

In countrary to what is said in [best practices](https://docs.cypress.io/guides/references/best-practices.html#Selecting-Elements), the context of RERO-ILS projects asks not to use specific attributes for DOM element selecting. Here is a list of selector we should use:


| Selectors | Example | Usage |
| --- | --- | ---|
| Id  | `cy.get('#main').click()` | Better |
| Name  | `cy.get('[name=submission]').click()` | Better |
| Text  | `cy.contains('Submit').click()` | Depends on translations |
| Specific attribute | `cy.get('[data-cy=submit]').click()` | To use only if there is no other way |

### Assertions

A list of assertions is available [here](https://docs.cypress.io/guides/references/assertions.html#BDD-Assertions).

## Tip & Tricks

### Testing an asynchronous app

In order to allow enough time to display the elements of the views, the default command timeout was set to 2 minutes.
In some cases, a better solutions is needed: wait on an request and on its response. Here is a basic example:
```
// Start a server
cy.server();

// Provide a route with an alias (this needs to be done early enough to start to listen to the route before using it)
cy.route({method: 'DELETE', url: '/api/items/*'}).as('deleteItem');

// Do something that matches the route defined above
cy.get('#item-' + this.itemBarcode + ' [name=buttons] > [name=delete]').click();
cy.get('#modal-confirm-button').click();

// Pass the route to wait for until the response
cy.wait('@deleteItem');

// The following commands will not run until the wait command resolves
cy.deleteRecordFromDetailView();
```

The documentation describing the network requests and corresponding subjects can be found [here](https://docs.cypress.io/guides/guides/network-requests.html)

### Change BaseURL without editing `cypress.json`

Use environment variable when you launch Cypress:

```bash
CYPRESS_BASE_URL=https://localhost:26375 cypress run
```
