# Invenio-circulation

`invenio-circulation` is a module used in RERO-ils to manage item loans.

RERO ILS uses a specific module to develop and enhance `invenio-circulation` module. You can find documentation on [RERO circulation module][1].

[1]: /circulation/circulation-module.md

## Install and test

You first need `invenio-circulation` branch from Github. Choose among one of:

* `git@github.com:inveniosoftware/invenio-circulation.git` (official)
* `git@github.com:rero/invenio-circulation.git` (ours)

```bash
git clone git@github.com:rero/invenio-circulation.git
cd invenio-circulation
```

Then install all needed dependencies (in **invenio-circulation** directory):

```bash
pipenv run pip install -r requirements-devel.txt
pipenv run pip install -e .[all,elasticsearch6,postgresql]
```

Check that your RERO-ils docker containers are launched (in **rero-ils** directory):

```bash
cd ../rero-ils
docker-compose up -d && ./docker/wait-for-services.sh
```

Finally you can launch `invenio-circulation` module **tests** like this (in **invenio-circulation** directory):

```bash
cd ../invenio-circulation
pipenv run python setup.py test
```

## Developing with rero-ils and invenio-circulation

In **rero-ils** directory (`git@github.com:rero/rero-ils.git` repository), you need to change **pyproject.toml**. Especially this line:

```toml
invenio-circulation = {tag = "v1.0.0a23", git = "https://github.com/inveniosoftware/invenio-circulation.git"}
```

* **tag** could be a branch name
* **git** should be changed by your repository path on Github (or elsewhere)

Then do:

```bash
poetry update invenio-circulation
```

This will install your repository from your github fork of invenio-circulation.
