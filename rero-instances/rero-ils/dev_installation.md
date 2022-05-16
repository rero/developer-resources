# Development environment

## Requirements

First install these tools on your operating system:

  * pyenv
  * nvm
  * pip
  * docker and docker-compose

Then install `poetry` and Python >3.9:

```bash
pyenv install 3.9.7
pip install --user poetry
```

## Preparation

At the end of this chapter your directory will look like this:

```
rero
├── ils
│   └── .env
├── ui
└── var
    └── ils
        └── invenio.cfg
```

Let's start:

```bash
# First directory creation
mkdir -p rero/var/ils
# Get rero-ils project
git clone git@github.com:rero/rero-ils.git rero/ils
# Set invenio configuration in another directory: /home/user/rero/var/ils/
echo "INVENIO_INSTANCE_PATH=${HOME}/rero/var/ils/" > rero/ils/.env
# Get rero-ils-ui project
git clone git@github.com:rero/rero-ils-ui.git rero/ui
# Send content to rero/var/ils/invenio.cfg file
cat >> rero/var/ils/invenio.cfg << EOF
ACCOUNTS_SESSION_REDIS_URL="redis://cache:6379/1"
BROKER_URL="amqp://guest:guest@mq:5672/"
CACHE_REDIS_URL="redis://cache:6379/0"
CELERY_BROKER_URL="amqp://guest:guest@mq:5672/"
CELERY_RESULT_BACKEND="redis://cache:6379/2"
SEARCH_ELASTIC_HOSTS=['es:9200']
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://rero-ils:rero-ils@db:5432/rero-ils"
RATELIMIT_STORAGE_URL="redis://cache:6379/3"

#APP_ENABLE_SECURE_HEADERS=False
#SESSION_COOKIE_SECURE=False
#WTF_CSRF_ENABLED=False

ENV='development'
DEBUG=True

RERO_ILS_MEF_HOST='mef.test.rero.ch'
RERO_ILS_MEF_URL="https://mef.test.rero.ch/api/mef/"

MAIL_SUPPRESS_SEND=1
EOF
```

## Installation

```bash
# working directory is rero-ils project
cd rero/ils
# Use Python 3.9.7
pyenv local 3.9.7
# Prepare environment: python dependencies, python development tools, etc.
poetry run poe bootstrap
# Launch Docker
docker-compose up -d && ./docker/wait-for-services.sh
# Setup our instance (-w to avoid python warnings, -C to add persons without using internet)
poetry run poe setup -C
```

## Usage

Launch rero-ils server:

```bash
poetry run poe server
```

# Reinstall development environment

We consider `rero-ils` project is located in **/home/user/rero/rero-ils** directory.

First we flush RERO Docker environment:

```bash
cd /home/user/rero/rero-ils
docker-compose down
docker rmi `docker images|grep rero| tr -s " "| cut -d " " -f 3` --force
docker volume prune --force
```

Then flush your poetry installation:

```
poetry env remove $(poetry env list|cut -d " " -f 1)
```

And bootstrap a new environment (~5 min):

```bash
poetry run poe bootstrap
```

Setup it (~23 min with -d, ~13 min without):

```bash
# -w reduces warnings, -C uses local persons and -d loads big data for deployment
docker-compose up -d && ./docker/wait-for-services.sh && poetry run poe setup -C -d
```

And finally launch server:

```bash
poetry run poe server
```

https://localhost:5000 and https://localhost:5000/professional/ should be available.
