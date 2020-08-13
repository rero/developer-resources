# Git and GitHub workflow

[github-cli][1] may help you in this workflow.

The main RERO ILS `git` repository has two main branches:

1. The `master` branch contains the last official release, tagged, which is
   deployed on [ils.test.rero.ch](https://ils.test.rero.ch).
1. The `dev` branch (default branch) contains the work being done during a
   sprint, or in between two releases. When on the `dev` branch a release is
   ready, the `dev` branch is pushed to `master`.

Each contributor has his or her own fork and opens a PR (pull request) using
either the `rero-ils/dev` branch as its base, or a specific `rero-ils` branch
corresponding to a specific US (user story).

This way, the development team is able to deploy a specific PR or a US branch
on the staging server, allowing the PO (product owner) to test a new
functionality.

## Adding remotes URL

1. Get the `git` remote repository URL you need to add.
1. `git remote add [name] [git remote repository URL]`

For the name, chose a name that you can easily memorize.

## Updating your branches

1. Fetch the changes:
    - `git fetch [remote name]` or
    - `git fetch [remote name] -p` (prune deleted branches) or
    - `git fetch --all` (fetch changes of all remotes) or
    - `git fetch --all -p` (fetch changes of all remotes and prune) or
1. Place yourself in the branch you want to update:
    - `git checkout [branch name]` or
    - `git switch [branch name]`
1. Update your branch:
    - `git pull [remote name] [branch name]` or
    - `git rebase [remote name]/[branch name]` or
    - `git reset --hard [remote name]/[branch name]` (this will overwrite all
      your local changes).

Very often, you'll need to rebase your working branch on the `dev` branch,
because the `dev` branch has move just before your PR opening or merging:

- `git switch [your working branch name]`
- `git rebase [main rero-ils remote name]/dev`

You may need to resolve conflicts.

[1]: https://cli.github.com/
