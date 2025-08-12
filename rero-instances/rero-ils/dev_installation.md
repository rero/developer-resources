# Development environment

## Requirements

First install these tools on your operating system:

* uv
* nvm
* docker and docker-compose

Then install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) and Python >3.9:

```bash
uv python install 3.12
```

## Preparation

Let's start by getting all projects:

```bash
# Clone the rero-ils project
git clone git@github.com:rero/rero-ils.git
# Clone the rero-ils-ui project
git clone git@github.com:rero/rero-ils-ui.git
# Clone ng-core
git clone git@github.com:rero/ng-core.git
```

## Backend installation

```bash
# working directory is rero-ils project
cd rero-ils
# Use Python 3.12
uv python pin 3.12
# Prepare environment: python dependencies, python development tools, etc.
uv run poe bootstrap
# Launch Docker
docker compose up -d
# Setup our instance (-w to avoid python warnings, -C to add persons without using internet)
uv run poe setup
```

If you want to go directly in uv's virtual environment, run `source .venv/bin/activate`. In the venv, you don't need to use `uv run` for each command.

## Usage

Launch rero-ils server:

```bash
uv run poe server
```

## Reinstall development environment

We consider `rero-ils` project is located in **/home/user/rero/rero-ils** directory.

First we flush RERO Docker environment:

```bash
cd /home/user/rero/rero-ils
docker-compose down
docker rmi `docker images|grep rero| tr -s " "| cut -d " " -f 3` --force
docker volume prune --force
```

Then delete your `.venv/` folder

And bootstrap a new environment (~5 min):

```bash
uv run poe bootstrap
```

Setup it (~23 min with -d, ~13 min without):

```bash
# -w reduces warnings, -C uses local persons and -d loads big data for deployment
docker-compose up -d && ./docker/wait-for-services.sh && uv run poe setup -C -d
```

And finally launch server:

```bash
uv run poe server
```

[https://localhost:5000](https://localhost:5000) and [https://localhost:5000/professional/](https://localhost:5000/professional/) should be available.
