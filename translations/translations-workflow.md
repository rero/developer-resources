# Translations workflow

## Introduction

We're using weblate as a web service to help the translation process, through
the hosted service of weblate: <https://hosted.weblate.org/projects/rero_plus>

For our needs, on Weblate, we have one project (named RERO+, with `rero_plus`
as slug), with several *components*:

- `ng-core`.
- `rero-ils`.
- `rero-ils-public-search` (from the project `rero-ils-ui`).
- `rero-ils-admin` (from the project `rero-ils-ui`).
- `rero-ils-shared` (from the project `rero-ils-ui`).
- `sonar`.
- `sonar-ui`.

## The regular workflow

### From a developer point of view

With this workflow, developers only need to add translation markers in the source code's translatable strings, or, when necessary, add string in the
*manual translation* file.

Testing the extraction to check the code is a good idea, though. But no files
should be modified in the translation folders and subfolders (ie
`rero_ils/translations` or `projects/admin/src/assets/rero-ils-ui/admin/i18n`).

### From the translation manager point of view

**We do not use the automatic workflow through the GitHub webhook, to avoid
conflicts.**

#### Push translations

Weblate :arrow_right: Github (`translations`)

*When translations have been updated on Weblate, we commit and push them to the Github `translations` branch. This is generally done before extracting new messages or right before a release but can be done at anytime during the sprint*

1. In the Weblate component, under `Manage`, `Repository Maintenance`: `Commit` all changes and `Push`.
2. This creates a PR in the Github `translations` branch. `Rebase and merge` this PR.

#### Prepare a release

Weblate :arrow_left: Github (`translations`) :arrow_left: Github (`staging`)

*when all PRs from a Release-Candidate have been merged into `staging`, we need to extract the messages and push them to Weblate so that they can be translated.*

1. Ensure that all Weblate changes have been committed and merged to `upstream/translations` ([see push translations](#push-translations)).
1. Lock the Weblate component so that no further changes are made.
1. Switch to your local `translations` branch and pull the changes from `upstream/translations`.
1. Rebase this branch onto staging `git pull --rebase upstream staging`.
1. On your local `translations`, extract the messages and check that everything looks good.
   1. Angular projects: `npm ci` to compile the project, `npm run extract_messages` to extract the strings from the code to the master messages file.
   2. Python projects: `poetry run python ./setup.py extract_messages` to extract the strings from the code to the master messages file.
1. Update the catalog so that all langugage files are updated.
   1. Angular projects: `npm run update_catalog --no-fuzzy-matching`
   2. Python projects: `poetry run python ./setup.py update_catalog --no-fuzzy-matching`
1. Commit with message `translations: extract messages`.
1. Force push your local `translations` branch to upstream with `git push upstream translations -f`.
1. Unlock the Weblate component.
1. In Weblate, use `Maintenance` -> `Reset` to force-sync Weblate and Github.
1. Check that the new strings have been added for translation.
1. Inform [the translation team](https://gitter.im/rero/reroils-translations) that there are new translations available.

Weblate :arrow_right: Github (`translations`) :arrow_right: Github (`staging`)

*When the translators have finished working on the release, we can push the changes from Weblate to `translations`, then to `staging`.*

1. Ensure that all Weblate changes have been committed and merged to `upstream/translations` ([see push translations](#push-translations)).
2. Lock the Weblate component so that no further changes are made.
3. Ensure that our local `staging` is up to date with `upstream/staging`.
4. Switch to your local `translations` branch and pull the changes from `upstream/translations`.
5. Ensure that your `translations` branch contains all commits from `staging`: `git rebase staging`.
6. If there are multiple translation commits, sqash them into one with `git rebase -i HEAD~4` (4 being the number of commits to sqash). See [this section](#commit-sqashing) for details.
7. Switch to `staging` and `git rebase translations`.
8. If everything went as expected, only your one translation commit has been added to the tree. Push upstream (`git push upstream staging`), without force push. If you can't regular push, this means your commit tree is incorrect.
9. Force-push your local `translations` branch to `upstream:translations` so that `staging` and translations are at the same commit.
10. In Weblate, use `Maintenance` -> `Reset` to force-sync Weblate and Github.
11. Unlock the Weblate component to allow translators to work.

#### Commit sqashing

Weblate creates one commit per language when pushing changes. In order to limit the number of commits created by Weblate in the repositories, translation commits are sqashed into one before being pushed back to `upstream/translations`. To simplify this process, the commit message should look like the following template:

```md
translations: translate vX.X.X

Translate-URL: https://hosted.weblate.org/projects/rero_plus/rero-ils/
# Adapt this link to the component

Co-Authored-by: Pascal Repond <pascal.repond@rero.ch>
# If needed, add all contributors that specifically participated to this particular commit (optional)
```

## Some weblate settings

- [component/settings/version control] Merge Style: rebase.
- [component/settings/version control] Age of changes to commit: 24 [hour].
- [rero_/#workflow] Source language: English (United States). This sets `en_US`
  as the source language file, in order to avoid translating it.
- [component/settings/files]: filter: `^(?!(en_US)$).+$` (for `ng-core`,
  `public-search`, `admin`). This is needed, as in our angular project, the
  source language file is the same as a translated language files.
- [component/settings/files]: filter: `^(?!(messages)$).+$` (for `sonar-ui`).
  The same as the previous setting, but adapted to the `sonar-ui`
  configuration.
- on each component, [addons]:
  - automatic translations, suggest strings for non translated strings, use
    machine translations (deepl, weblate, weblate translation memory), with
    80 thresold.
  - squash git commits, per language, add contributors in the commit message,
    copy paste the regular commit message.
  - only for JSON based component, customize JSON output, with 2 space for
      indentation.

## Troubleshooting

- If, for any reason, the github branch that has been defined as a weblate
  corresponding branch (Composant settings, Version control, Repository
  branch), has been forced push, **use the reset command either on the weblate
  web interface, or with the `wlc` client**.
- At leat once, changes couldn't be committed if the remote repository branch
  moved. Apparently weblate wait until the local branch is up to date with the
  remote branch *before* committing changes. Changes that aren't committed will
  be lost when the local branch is going to be updated. **As a result, we use a translation dedicated branch on the remote repository (github)**.

## Tips for the translators

- Have a look, even shortly to the [weblate documentation][9]:
  - Especially on [*Translating using Weblate*][10].
- In each component, a language is the source code. It is in a darker green and
  has a specific icon: this language should not be translated, of course.
- On the language overview of each component, there are some links to strings
  grouped by status: translated, to be reviewed, needing actions, and so on.
  This is actually useful.
- In the same spirit, once a string is selected,
  - on the right of the editor, you may have some information: on top a
    glossary, if any, and on the bottom links to the source code, if it can
    help to understand the context.
  - below the left section, there are some tabs:
    - nearby strings, which sometimes can help have a context,
    - other occurences, which helps to be coherent,
    - comment,
    - machinery, which can provide automatic suggestions,
    - other languages, to check how this string is translated in other
      languages,
    - history.

![Weblate Summary](intro_weblate.jpg)

[9]: https://docs.weblate.org
[10]: https://docs.weblate.org/en/latest/user/translating.html
