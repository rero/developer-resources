# Generating a changelog

Use [github-changelog-generator][1].

It's a ruby software that reads a github project event data through github's
API and generate a changelog with sections about fixed bugs (issues with the
bug tag), fixed issues, and merge PR.

:warning: **The [project
README][2] is very informative on the installation method and usage.**

[1]: https://github.com/github-changelog-generator/github-changelog-generator
[2]: https://github.com/github-changelog-generator/github-changelog-generator/blob/master/README.md

## Install

Ruby >3.0.0 is required. Install it for your OS. For Linux, [rbenv](https://github.com/rbenv/rbenv) is a good way to choose the Ruby version.

Install `github_changelog_generator`:

    gem install github_changelog_generator

Of course, to update:

    gem update github_changelog_generator

## Usage

### GitHub's API Token

You need to generate a *personal access token* to avoid the API's limit. You
can do that on <https://github.com/settings/tokens>.

You also need the correct permissions on the repository for which you want to
read the events through the API.

### Generating the changelog

All versioned projects should contain a param file `.github_changelog_generator`, which sets the parameters (repo, branch, file structure, tags to ignroe, etc.). You can adapt this file to your needs.

To update the `CHANGELOG.md` file with a new release, use this command with the corresponding parameters:

    github_changelog_generator --since-tag <latest published release> --future-release <new release> -t <github token>

For example, the following command will look at all changes (issues and PRs) between the tag `v1.9.5` and the current state of your branch. It will name this section `v1.10.0`:

    github_changelog_generator --since-tag v1.9.5 --future-release v.1.10.0 -t DgDmTBkmRQoZZCMj985ueFKbPkXeLbvRtCyTJZFi

### Verification

1. After generating a changelog, check carefully that:
   * Only the new release has been added to the `CHANGELOG.md` file
   * Nothing else has been deleted from the file
   * The listed issues and PRs correspond to the ones that have been closed/merged for this release (not more, not less!)
1. Manually fix any blatantly unclear or non-pertinent info in the generated list. Sometimes issues are closed wihtout being fixed. If someone closed an issue and forogt to tag it as `stale`, `wontfix` or `duplicate`, the generator will add it to the changelog.
1. Once everything looks fine, save the file and keep on with the release!
