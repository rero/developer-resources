# Poetry

Poetry is a free and open source python packaging and dependency management system.

It's an alternative to the famous [pipenv](https://pipenv.pypa.io/en/latest/) command.

# Main commands

Basic commands:

```bash
poetry env list # gets virtualenv for current project
poetry add pendulum # adds pendulum as new dependency for current project
poetry update # updates dependencies to their latest compatible versions and create poetry.lock again
poetry config --list # gets poetry config. parameters
poetry config virtualenvs.path /home/user/other/path # change virtualenvs default path for ALL projects
poetry config virtualenvs.path /home/project/my_venv --local # change CURRENT PROJECT virtualenv default path
poetry run invenio --help # runs `invenio --help` in a virtualenv from the current project
```

# Configuration

`poetry config --list` gives you :

```
cache-dir = "/home/od/.cache/pypoetry"
virtualenvs.create = true
virtualenvs.in-project = false
virtualenvs.path = "{cache-dir}/virtualenvs"  # /home/od/.cache/pypoetry/virtualenvs
```

To change a value: `poetry config parameter new_value`. This will change the value **globally**: for all projects that uses poetry.

For example: `poetry config virtualenvs.in-project true` will always create virtualenvs in project directory.

To change the value **only for the current project**, simply add `--local` (i.e. `poetry config virtualenvs.in-project true --local`).

To reset a value: `poetry config virtualenvs.path --unset`. Change *virtualenvs.path* with the parameter you want to reset.

# Tips

## Keep configuration in a specific project

You can use a **poetry.toml** file with a content similar to:

```toml
[virtualenvs]
create = true
in-project = true
path = "/home/user/project/.venv"
```

## Remove all current project virtual environments

```bash
poetry env remove $(poetry env list|cut -d " " -f 1)
```

# References

* [Official documentation](https://python-poetry.org/docs/)
