# How to publish a new release?

This page describes the process that we use to publish a new release of the RERO+ projects.

## RERO ILS/SONAR

1. **Release the other projects:**
   1. If needed, publish a release for [ng-core](#ng-core) and [rero-ils-ui OR sonar-ui](#rero-ils-uisonar-ui)
2. **Prepare a release-candidate:**
   1. Decide what you want to integrate into the new release and merge everything into a branch to be used as a release-candidate (usually `staging`).
   2. Deploy the state of this branch to `test` or `dev` servers for internal testing.
3. **Translate the release:**
   1. Extract the new translations to [Weblate][3] and give the conrtributors some time to translate the new strings; then, integrate the translation commit. [See detailed translation workflow][2].
4. **Prepare a release commit:**
   1. Make sure your local repository is up to date with remote (`git fetch -p --all`).
   2. Update `scripts/bootstrap` with the `rero-ils-ui` OR `sonar-ui` used version.
   3. Update `rero_ils/version.py` OR `sonar/version.py`.
   4. Update `pyproject.yml`.
   5. Update the `CHANGELOG.md` file [as described here][1].
   6. Commit with message `release: v1.X.X`
   7. Open a Pull Request for the release on the Github repository.
5. **Publish to `master`:**
   1. When the release PR is merged into `staging`, update your local `staging` branch, verify carefully that the commits, commit hashes are the same.
   2. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   3. Merge your local `staging` branch into your local `master`: `git merge --ff-only staging`. Check that your `staging` and `master` are up to date with `upstream/staging`.
   4. Tag the last commit: `git tag -m "v1.X.X" v1.X.X`.
   5. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   6. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.

## RERO ILS UI/SONAR UI

1. **Translate the release:**
   1. Usually at the same time than the translation for the backend project.
   2. Extract the new translations to [Weblate][3] and give the conrtributors some time to translate the new strings; then, integrate the translation commit. [See detailed translation workflow][2].
2. **Prepare a release commit:**
   1. Check that:
      - the dev branch contains all PRs and branch planned for the release
      - the translations are up to date
      - the `ng-core` version is the latest (if needed, publish a new version of [ng-core](#ng-core)).
   2. Update the `version` property in `package.json` file.
   3. Run the command `npm i` to update `package-lock.json` file.
   4. Update the `CHANGELOG.md` file [as described here][1].
   5. Commit with message `release: v1.X.X`
   6. Open a Pull Request for the release on the Github repository.
3. **Publish NPM package (usually done by a developer)**
   1. Checkout to your local `staging` branch, make sure it's up to date with the
   remote `staging`.
   1. Build library with the command `npm run pack` (from the project's root).
   1. Navigate to the `/build` directory and execute `npm publish` to publish library in npm registry. You must be logged in npm and the user has to belong to `rero` organisation (Check with IT to get access).
4. **Publish to `master`:**
   1. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   2. Merge the `staging` branch into master: `git merge --ff-only dev`.
   3. Tag the last commit: `git tag -m "v1.X.X" v1.X.X`
   4. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   5. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.

## NG-CORE

1. **Prepare a release commit:**
   1. Update the `version` property in `package.json` file.
   2. Update the `version` property in `projects/rero/ng-core/package.json` file.
   3. Run the command `npm i` to update `package-lock.json` file.
   4. Commit the changes to `staging` or on a specific branch and specify changes in commit message.
   5. Push or PR the release commit to `upstream/staging`.
2. **Publish NPM package (usually done by a developer)**
   1. Checkout to your local `staging` branch, make sure it's up to date with the remote `staging`.
   2. Build library with the command `ng build @rero/ng-core`.
   3. Go to generated library with command `cd dist/rero/ng-core`.
   4. Check version is correct in `package.json` in the current folder.
   5. Execute `npm publish` to publish library in npm registry. You must be logged in npm and the user has to belong to `rero` organisation (Check with IT to get access).
3. **Publish release to `master`**
   1. Go back to root folder.
   2. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   3. Merge the `staging` branch into master: `git merge --ff-only dev`.
   4. Tag the last commit: `git tag -m "v0.X.X" v0.X.X`.
   5. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   6. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.

[1]: ../documentation/generate-changelog.md
[2]: ../translations/translations-workflow.md
[3]: https://hosted.weblate.org/projects/rero_plus/
