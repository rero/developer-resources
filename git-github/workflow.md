# Git and GitHub workflow

:warning: [github-cli][1] may help you in this workflow, especially to view or
test PRs of other contributors. You're encouraged to discover it's
possibilities.

## Main branches

The main RERO ILS `git` repository has two main branches:

1. The `master` branch stays at the last official release tag.
1. The `staging` branch (default branch) contains the work being done during a
   sprint, between two releases. When the `staging` branch is ready for a
   release, the `staging` branch is pushed into `master`. \
   **When a release is ready or needed, depending on the
   presence or absence of new features**, a minor or a patch is published.

Mostly, the PRs will be based on the default branch, that is the `staging`
branch, except when a user story branch is used.

## Deployment branches

Basically, there's as many branches as servers. For each branch, there's an
image on Docker Hub:

- for [ils.test.rero.ch][demo]: `ils_test`.
- for [ilsdev.test.rero.ch][dev]: `ils_dev`.
- for [bib.test.rero.ch][test]: `bib_test`.

Each deployment branch is built as needed, especially the `ils_dev` branch that
may contain all the commits that need to be tested. On these branches, force
pushing is not an issue, as they aren't used for development.

For the production server, they are at least three branches, allowing to
quickly revert to a precedent version: latest and two precedent tags.

- for [bib.rero.ch][prod]: `bib-latest`, `bib-1.4.10`, `bib-1.4.9` (for
  example, here the latest being the `v1.4.11`), corresponding to three images
  on Docker Hub.

### Critical bug fix

When a critical bug needs to be fixed as quick as possible, a branch is created
from the last tag in production (usually the master branch), named
`<last-tag>-fix`. This branch will contain the fix. Depending on the situation,
then this commit will need to be added to the `staging` branch too.

### Publishing a release

When a less critical bug is fixed by a commit on the `staging` branch, a
release is published, which could be a minor or a patch version.

When reaching the end of the current sprint, a release may be published.
Depending on breaking changes, it may be a major or a minor version.

## From a contributor point of view

Each contributor has his or her own fork and opens a PR (pull request) using
either the `rero-ils/staging` branch as its base, or a specific branch
corresponding to a user story (US), such as `rero-ils/US-<name>`.

### Updating your branches

1. Fetch the changes:
    - `git fetch --all -p` (fetch changes of all remotes and prune).
1. Place yourself in the branch you want to update:
    - `git checkout [branch name]` or
    - `git switch [branch name]`.
1. Update your branch:
    - `git pull [remote name] [branch name]` or
    - `git rebase [remote name]/[branch name]` or
    - `git reset --hard [remote name]/[branch name]` (this will overwrite all
      your local changes).

Very often, you'll need to *rebase* your working branch on the `staging`
branch, because the `staging` branch has moved just before your PR opening or
merging:

- `git switch <your-working-branch-name>`
- `git rebase <main-rero-ils-remote-name>/dev`

You may need to resolve conflicts.

[1]: https://cli.github.com/
[demo]: https://ils.test.rero.ch
[dev]: https://ilsdev.test.rero.ch
[test]: https://bib.test.rero.ch
[prod]: https://bib.rero.ch
