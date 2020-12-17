# Translations workflow

## Table of content

1. [Introduction][6]
1. [The regular workflow][3]
1. [Some weblate settings][5]
1. [Troubleshootings][11]
1. [Tips for the translators][8] 

## Introduction

We're using weblate as a web service to help the translation process, through
the hosted service of weblate: https://hosted.weblate.org/projects/rero_plus

For our needs, on weblate, we have one project (named RERO +, with `rero_plus`
as slug), with many *components*:

- `ng-core`.
- `rero-ils`.
- `rero-ils-public-search` (from the GitHub `rero-ils-ui`).
- `rero-ils-admin` (from the GitHub `rero-ils-ui`).
- `sonar`.
- `sonar-ui`.

## The regular workflow

**We do not use the automatic workflow through the GitHub webhook, to avoid
conflicts.**

The starting situation is just after a release: the GitHub `translations` branch
is on the same commit than the [weblate]][12] `translations` branch. Also, the
GitHub `translations` branch is on the same commit than the GitHub `dev`
branch.

1. Some changes are done on the `dev` branch.
1. Some changes are done on weblate.
1. Ensure that on weblate, all changes is committed.
1. Lock the component.
1. Then ensure that on GitHub all translations pull requests are merged into
   `translations` branch.
1. Fetch and pull new upstream commits (`translations` branch) on your local
   `translations` branch.
1. Maybe, you want to squash several commits into one.
1. Fetch new upstream commits (`dev` branch).
1. Rebase your `translations` branch on the upstream `dev` branch.
1. Extract messages, check that everything looks good.
1. Commit the changes in the already existing commit (`git amend`), to avoid
   adding a supplementary commit.
1. Update catalogs.
1. Commit changes in the precedent translation commit.
1. Force push the `translations` branch upstream (`translations` branch too).
1. On weblate, through the repository management settings, reset the weblate
   branch on the GitHub `translations` branch (The red *maintenance* dropdown
   menu).
1. Unlock the component.
1. Inform on the translations Gitter room that the component is updated and
   open to translation.
1. Repeat once a week, or when several US are merged into `dev` during the
   sprint.
1. Before release process, and even a few day before, when every weblate
   changes and every `dev` branch changes are into the `translations` branch,
   switch to the `dev` branch and `git merge --ff-only` the `translations`
   branch on it. If everything went as expected, you can then push upstream.
1. The `dev` branch can be deployed (or tested locally before) to be tested.
1. After the release, be sure to update the `translations` branches locally and
   on weblate, of course.

## Some weblate settings

- [component/settings/version control] Merge Style: rebase.
- [component/settings/version control] Age of changes to commit: 24 [hour].
- [rero_/#workflow] Source language: English (United States). This sets `en_US`
  as the source language file, in order to avoid translating it.
- [component/settings/files]: filter: `^(?!(en_US)$).+$` (for `ng-core`,
  `public-search`, `admin`). This is needed, as in our angular project, the
  source language file is the same as a translated language files.
- [component/settings/files]: filter: `^(?!(messages)$).+$` (for `sonar-ui`).
  The same as the precedent setting, but adapted to the `sonar-ui`
  configuration.
- on each component, [addons]:
    - automatic translations, suggest strings for non translated strings, use
      machine translations (deepl, weblate, weblate translation memory), with
      80 thresold.
    - squash git commits, per language, add contributors in the commit message,
      copy paste the regular commit message.
    - only for JSON based component, customize JSON output, with 2 space for
      indentation.

## Troubleshootings

- If, for any reason, the github branch that has been define as a weblate
  corresponding branch (Composant settings, Version control, Repository
  branch), has been forced push, **use the reset command either on the weblate
  web interface, or with the `wlc` client**.
- At leat once, changes couldn't be committed if the remote repository branch
  moved. Apparently weblate wait until the local branch is up to date with the
  remote branch *before* committing changes. Changes that aren't committed will
  be lost when the local branch is going to be updated. **As a result, we may
  need a translation dedicated branch on the remote repository (github)**.

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

![](intro_weblate.jpg)

[1]: https://docs.weblate.org/en/latest/admin/continuous.html#automatically-receiving-changes-from-github
[2]: https://docs.weblate.org/en/latest/admin/continuous.html#avoiding-merge-conflicts
[3]: #the-regular-workflow
[4]: https://docs.weblate.org/en/latest/wlc.html
[5]: #some-weblate-settings
[6]: #introduction
[7]: #the-very-first-time
[8]: #tips-for-the-translators
[9]: https://docs.weblate.org
[10]: https://docs.weblate.org/en/latest/user/translating.html
[11]: #troubleshootings
[12]: https://hosted.weblate.org/projects/rero_plus/
