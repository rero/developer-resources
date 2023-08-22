# How to publish a new release?

This page describes the process that we use to publish a new release of the RERO+ projects.

## RERO ILS/SONAR

1. **Release the other projects:**
   1. If needed, publish a release for [ng-core](#ng-core) and [rero-ils-ui OR sonar-ui](#rero-ils-uisonar-ui)
2. **Prepare a release-candidate:**
   1. Decide what you want to integrate into the new release and merge everything into a branch to be used as a release-candidate (usually `staging`).
   2. Optionnally, deploy the state of this branch first to `dev` servers for internal testing.
3. **Translate the release:**
   1. Extract the new translations to [Weblate][3] and translate the new strings; then, integrate the translation commit to `staging`. [See detailed translation workflow][2].
4. **Prepare a release commit:**
   1. Make sure your local repository is up to date with remote (`git fetch -p --all`).
   2. Upadte UI version:
      - ILS: Update `scripts/bootstrap` with the `rero-ils-ui` version.
      - SONAR: update to the correct `sonar-ui` version in `sonar/config_sonar.py` > `SONAR_APP_UI_VERSION`
   3. Update `rero_ils/version.py` OR `sonar/version.py`.
   4. Update `pyproject.toml` with the version number.
   5. Update the `CHANGELOG.md` file [as described here][1].
   6. Commit with message `release: v1.X.X`
   7. Open a Pull Request for the release on the Github repository (the tests will fail as long as the UI version is not published on NPM).
   8. Force push the state of the release branches for all the project to the test branch (`bib-test`)
   9. Devs prepare the images and the data migration scripts and deploy the release to the test branch.
   10. Test the release thouroughly and fix any problems with new commits.
5. **Publish to `master`:**
   1. When the release has been tested and validated and fixes and release PR are merged into `staging`, update your local `staging` branch, verify carefully that the commits, commit hashes are the same.
   2. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   3. Merge your local `staging` branch into your local `master`: `git rebase staging`. Check that your `staging` and `master` are up to date with `upstream/staging`.
   4. Tag the last commit: `git tag -m "v1.X.X" v1.X.X`.
   5. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   6. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.
   7. Update all branches that need to contain the latest release (e.g. `ils-test`, etc)
   8. Deploy the release in production

## RERO ILS UI/SONAR UI

1. **Translate the release:**
   1. Usually at the same time than the translation for the backend project.
   2. Extract the new translations to [Weblate][3] and translate the new strings; then, integrate the translation commit to `staging`. [See detailed translation workflow][2].
2. **Prepare a release commit:**
   1. Check that:
      - the `staging` branch contains all PRs and branches planned for the release
      - the translations are up to date
   2. Update the `version` property in `package.json` file.
   3. Update the `ng-core` version in `package.json` file if you use a new version of `ng-core`.
   4. Run the command `npm i` to update `package-lock.json` file (the ng-core version must be published to NPM).
   5. Update the `CHANGELOG.md` file [as described here][1].
   6. Commit with message `release: v1.X.X`
   7. Open a Pull Request for the release on the Github repository.
3. **Publish to `master`:**
   1. When the release PR is merged into staging and has been tested, checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   2. Merge the `staging` branch into master: `git rebase staging`.
   3. Tag the last commit: `git tag -m "v1.X.X" v1.X.X`
   4. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   5. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.
4. **Publish NPM package (usually done by a developer)**
   1. Checkout to your local `master` branch, make sure it's up to date with the
   remote `master`.
   1. Build library with the command `npm run pack` (from the project's root).
   1. Navigate to the `/build` directory and execute `npm publish` to publish library in npm registry. You must be logged in npm and the belong to `rero` organisation (Check with IT to get access).

## NG-CORE

1. **Prepare a release commit:**
   1. Update the `version` property in `package.json` file.
   2. Update the `version` property in `projects/rero/ng-core/package.json` file.
   3. Run the command `npm i` to update `package-lock.json` file.
   4. Update the `CHANGELOG.md` file [as described here][1].
   5. Commit the changes to `staging` or on a specific branch and specify changes in commit message.
   6. PR+merge the release commit to `upstream/staging`.
2. **Publish release to `master`**
   1. Go back to root folder.
   2. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   3. Merge the `staging` branch into master: `git rebase staging`.
   4. Tag the last commit: `git tag -m "v0.X.X" v0.X.X`.
   5. Push the local `master` branch to remote, with the tag: `git push --tags [rero-remote-repository-name] master`.
   6. On Github, edit the corresponding tag (that means publishing a new release) with title `v1.X.X`. Copy paste the corresponding changelog from `CHANGELOG.md` to the description.
3. **Publish NPM package (usually done by a developer)**
   1. Checkout to your local `master` branch, make sure it's up to date with the remote `master`.
   2. Build library with the command `ng build @rero/ng-core`.
   3. Go to generated library with command `cd dist/rero/ng-core`.
   4. Check version is correct in `package.json` in the current folder.
   5. Execute `npm publish` to publish library in npm registry. You must be logged in npm and belong to `rero` organisation (Check with IT to get access).

[1]: ./generate-changelog.md
[2]: ../translations/translations-workflow.md
[3]: https://hosted.weblate.org/projects/rero_plus/
