# How to publish a new release?

## RERO ILS

1. In another PR/commit, verify that there's no more strings to be extracted,
   that the available transifex translations have been integrated.
1. Update, if necessary, `rero_ils/bundles.py` with the `rero-ils-ui` used
   version.
1. Update `rero_ils/version.py`.
1. Update `pyproject.yml`.
1. Update the `CHANGES.rst` file (check 
   [how to generate it][1]. To do this, you need to be
   sure that no PR will be added to the `dev` branch.
1. Update the `RELEASE-NOTES.rst`:
    - Write a release notes (summary of the commits) in a MD file.
    - Convert the Markdown in ReStructuredText with `pandoc`:
  `pandoc -t rst --reference-links -o <destination>.rst <your-file>.md`.
    - Copy the content of the `.rst` file as a new section in the
  `RELEASE-NOTES.rst`.
    - Of course, do not add to the `git` history your working files.
1. Once everything is ready, propose a PR, make sure the release note is
   specifically reviewed.
1. When this PR is merge into `dev`, update your local `dev` branch, verify
   carefully that the commits, commit hashes are the same.
1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
1. Merge the `dev` branch into master: `git merge --ff-only dev`.
1. Tag the last commit: `git tag -s -m "v0.X.X" v0.X.X`. (`-s` is to sign the
   tag with your GPG key, it's optional).
1. Push the local `master` branch to remote, with the tag: `git push --tags
   <rero-remote-repository-name> master`.
1. On github, edit the corresponding tag with the following content, adapted to
   your situation: "Find the comprehensive release note on the RELEASE-NOTES.rst
   file: https://github.com/rero/rero-ils/blob/master/RELEASE-NOTES.rst#v0XX" 
   and publish it as release.

[1]: /documentation/generate-changelog.md

## RERO ILS UI

:construction: To be completed.

## NG-CORE

1. Update the `version` property in `package.json` file.
1. Update the `version` property in `projects/rero/ng-core/package.json` file.
1. Run the command `npm i` to update `package-lock.json` file.
1. Commit the changes on dev or on a specific branch and specify changes in 
   commit message.
1. If a pull request is created and validated, merge it into `dev`.
1. Checkout to your local `dev` branch, make sure it's up to date with the
   remote `dev`.
1. Build library with the command `ng build @rero/ng-core`.
1. Go to generated library with command `cd dist/rero/ng-core`.
1. Check version is correct in `package.json` in the current folder.
1. Execute `npm publish` to publish library in npm registry. You must be logged 
   in npm and the user has to belong to `rero` organisation (Check with IT to get access).
1. Go back to root folder.
1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
1. Merge the `dev` branch into master: `git merge --ff-only dev`.
1. Tag the last commit: `git tag -s -m "v0.X.X" v0.X.X`. (`-s` is to sign the
   tag with your GPG key, it's optional).
1. Push the local `master` branch to remote, with the tag: `git push --tags
   <rero-remote-repository-name> master`.
