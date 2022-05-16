# Generating a changelog

Use [PyChangelog][1].

It's a Python tool that reads a github project event data through github's
API and generate a changelog with sections about fixed bugs (issues with the
bug tag), fixed issues, and merged PRs.

[1]: https://github.com/rero/pychangelog

## Install

1. Clone the repo : `git clone https://github.com/rero/pychangelog.git`.
2. Run `poetry install` to install dependencies.

## Usage

1. Edit the following in `config.ini`:
   1. `repo`: the name of the project (`rero-ils`, `rero-ils-ui`, `sonar`, ...)
   2. `from_tag` and `to_tag`: Title of latest release (e.g. `v1.10.0`) and 
   title of next release (e.g. `v1.11.0`).
2. Run `poetry run ./changelog.py --token <your-github-token>`
3. Check `PYCHANGELOG.md` for your changelog
4. Copy the generated changelog from `PYCHANGELOG.md` to the top of your 
project's `CHANGELOG.md`.

### Verification

1. After generating a changelog, check carefully that:
   * Only the new release has been added to the `CHANGELOG.md` file
   * The listed issues and PRs correspond to the ones that have been 
   closed/merged for this release (not more, not less!)
2. Manually fix any blatantly unclear or non-pertinent info in the generated 
list. If necessary, edit the issue directly in Github and generate the 
changelog again. Sometimes issues are closed wihtout being fixed. If someone 
closed an issue and forogt to tag it as `stale`, `wontfix` or `duplicate`, the 
generator will add it to the changelog.
3. Once everything looks fine, save the file and keep on with the release!

### GitHub's API Token

You need to generate a *personal access token* to avoid the API's limit. You
can do that on <https://github.com/settings/tokens>.

You also need the correct permissions on the repository for which you want to
read the events through the API.
