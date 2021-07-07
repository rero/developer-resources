# How to publish a new release?

## RERO ILS

1. In the `translations` branch, verify that there's no more strings to be
   extracted, and that the available [weblate][3] translations have been
   integrated. See the [weblate workflow][2]. Make sure this PR or commit is
   integrated to the `dev` branch before integrating the release commit
   (below).
1. Make sure your local repository is up to date with remote (`git fetch`).
1. Update `scripts/bootstrap` with the `rero-ils-ui` used version.
1. Update `rero_ils/version.py`.
1. Update `pyproject.yml`.
1. Update the `CHANGES.md` file (check 
   [how to generate it][1]. To do this, you need to be sure that no PR will be
   added to the `dev` branch.
1. Update the `RELEASE-NOTES.rst` :
    - Write a release notes (summary of the commits) in a MD file (or directly
      in ReStructuredText if you can). Read the `rero/rero-ils`,
      `rero/rero-ils-ui` and `rero/ng-core` (at least what is relevant for ILS)
      commits since the last existing tag.
    - Convert the Markdown in ReStructuredText with `pandoc`: `pandoc -t rst
      --reference-links -o <destination>.rst <your-file>.md`.
    - Copy the content of the `.rst` file as a new section at the top of the
      `RELEASE-NOTES.rst`.
    - Of course, do not add to the `git` history your working files.
1. Once everything is ready, propose a PR.
1. When this PR is merge into `dev`, update your local `dev` branch, verify
   carefully that the commits, commit hashes are the same.
1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
1. Merge your local `dev` branch into your local `master`: `git merge --ff-only dev`.
1. Tag the last commit: `git tag -s -m "v0.X.X" v0.X.X`. (`-s` is to sign the
   tag with your GPG key, it's optional).
1. Push the local `master` branch to remote, with the tag: `git push --tags
   <rero-remote-repository-name> master`.
1. On github, edit the corresponding tag (that means publishing a new release)
   with the following content, adapted to your situation: "Find the
   comprehensive release note on the RELEASE-NOTES.rst file:
   https://github.com/rero/rero-ils/blob/master/RELEASE-NOTES.rst#v0XX" and
   publish it as release. You also need to give a title to the release, until
   now we've just entitled the release with the version number.

[1]: /documentation/generate-changelog.md
[2]: /translations/translations-workflow.md
[3]: https://hosted.weblate.org/projects/rero_plus/

## RERO ILS UI

1. Check that:
   - the dev branch contains all PRs and branch planned for the release
   - the traductions are up to date
   - the `ng-core` version is the latest (on the `ng-core` project).
1. Update the `version` property in `package.json` file.
1. Run the command `npm i` to update `package-lock.json` file.
1. Update the changelog (check [how to generate it][1]).
1. Commit the changes on dev or on a specific branch with the following commit
   message: `release: vx.x.x`.
1. If a pull request is created and validated, merge it into `dev`.
1. Checkout to your local `dev` branch, make sure it's up to date with the
   remote `dev`.
1. Build library with the command `npm run pack`.
1. Execute `npm publish` to publish library in npm registry. You must be logged
   in npm and the user has to belong to `rero` organisation (Check with IT to
   get access).
1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
1. Merge the `dev` branch into master: `git merge --ff-only dev`.
1. Tag the last commit: `git tag -s -m "v0.X.X" v0.X.X`. (`-s` is to sign the
   tag with your GPG key, it's optional).
1. Push the local `master` branch to remote, with the tag: `git push --tags
   <rero-remote-repository-name> master`.

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
   in npm and the user has to belong to `rero` organisation (Check with IT to
   get access).
1. Go back to root folder.
1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
1. Merge the `dev` branch into master: `git merge --ff-only dev`.
1. Tag the last commit: `git tag -s -m "v0.X.X" v0.X.X`. (`-s` is to sign the
   tag with your GPG key, it's optional).
1. Push the local `master` branch to remote, with the tag: `git push --tags
   <rero-remote-repository-name> master`.
