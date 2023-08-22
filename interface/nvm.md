# NVM

NVM stands for Node Version Manager. It consists in managing multiple version of NodeJS in your different projects.

More details can be found on [official NVM project page on Github](https://github.com/nvm-sh/nvm), especially for installation.

## Use

In all cases you should be in the working directory before launching any command.

## Compatible versions

To work on rero-ils and rero-ils-ui with maximal compatibility, we recommend using the following versions of NodeJS:

- `>v14.15.0`, `<v16.0.0`

:warning: When switching node versions in a backend application, run `poetry run invenio webpack clean`.

## In brief

```bash
# list available NodeJS version on your computer
nvm ls
# list all version that exists
nvm ls-remote
# install a specific version
nvm install lts/dubnium
# display current activated NodeJS version
nvm current
```

## Tips & Tricks

### Migration

If you migrate from a version to another, process like that:

```bash
# check which version you have (for example 10.16.3)
nvm current
# migrate from current version to the next one
nvm install lts/erbium --reinstall-packages-from=10.16.3
# uninstall useless version
nvm uninstall 10.16.3
# update package.json
npm i
# upgrade your environment
npm ci
```
