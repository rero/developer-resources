# Generating a changelog

You could use
[github-changelog-generator](https://github.com/github-changelog-generator/github-changelog-generator).

It's a ruby software that reads a github project event data through github's
API and generate a changelog with sections about fixed bugs (issues with the
bug tag), fixed issues, and merge PR.

:warning: **The [project
README](https://github.com/github-changelog-generator/github-changelog-generator/blob/master/README.md)
is very informative on the installation method and usage.**

## Installation

As it is a ruby software:

    gem install github_changelog_generator

Of course, to update:

    gem update github_changelog_generator

## Usage

This is how [@iGormilhit](https://github.com/iGormilhit) is using it, it could
certainly be improved or automated.

### GitHub's API Token

You need to generate a *personal access token* to avoid the API's limit. You
can do that on https://github.com/settings/tokens.

You also need the correct permissions on the repository for which you want to
read the events through the API.

### Generating the changelog

**:warning: `github_changelog_generator` generate files in Markdown format**.
You may need to convert it to another format, such as reStructuredText.

```bash
github_changelog_generator --user rero --project rero-ils -t <token> --release-branch dev --future-release v0.7.0 -o CHANGELOG.md
```

This will generate the `CHANGELOG.md` file for the first time (`-o
CHANGELOG.md`), for the `rero/rero-ils` project, using the user `rero`, but my
own token. It tracks the events that happened on the `dev` branch, specifies
the name of the next release (otherwise last changes, after the last tag, would
be in an "unrealesed" section). Finally, it specifies the output file.

But if you just want to add a section with the future new release, you could do
as follows:

```bash
github_changelog_generator --user rero --project rero-ils -t <token> --release-branch dev --future-release v0.7.0 -b CHANGELOG.md -o CHANGELOG.md
```

This command adds the `-b` parameter which specifies the already existing file
that will be expanded.

### License and format conversion

Since in RERO projects we have a License header, for the moment I suggest to
add it manually. **But you need to think about it**.

As written above, in the python projects, such as `rero-ils` adding the license
is not enough, the Markdown file have to be converted into reStructuredText.
For this, `pandoc` is the Swiss knife to use.

To install `pandoc`, see [the `pandoc`
documentation](https://pandoc.org/installing.html)

To convert a Markdown file into reStructuredText:

    pandoc -t rst -o <output.rst> <input.md>


