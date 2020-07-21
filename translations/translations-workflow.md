# Translations workflow

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

## The *very* first time

When every existing PR that contains modifications on the translated files are
merged into the `dev` branch of the corresponding GitHub project:

1. Verify that the weblate component is up to date with the GitHub project. To
   do that you can either:
    - Got to https://hosted.weblate.org/projects/rero_plus/ng-core/#repository
      (change `ng-core` to your needs) and check the repository status.
    - Or clone the weblate `git` repository and inspect the `git` logs (`git
      clone
      'https://hosted.weblate.org/git/rero_plus/<component>/')`.
    If it not, check [the workflow][3] below, to know how to update it.
2. Verify that on the GitHub repository settings, the webhook is active.
3. Unlock the translations (you can do that on the web interface, or through
   the [`wlc` client][4]).
4. Inform the translators that weblate is ready.

## The regular workflow

For the synchronisation workflow, it's semi automatic:

- A GitHub application is installed in the RERO GitHub organization.
- In each repository, a web hook is configured, as [explained in the weblate
  documentation][1].

This ensures two things:

1. As changes are merged into the `dev` branch of our repository, the weblate
   service is informed through the webhook and pulls changes to the weblate
   `git` repository. It's done with a `git rebase` command, as it can be
   configured in the component settings [component/settings/version control].
1. As translations are being made through the weblate interface, commits are
   being made. 24 hours after a commit ([see settings section][5]), a PR is
   created on the corresponding GitHub repository (called *upstream* by the
   weblate documentation).

As it is managed with `git`, and as we use *bilingual* files (each translation
files has two languages), which supposes to update the catalogs, conflicts can
happen. To avoid such conflicts, [the documentation][2] proposes something like
the following:

*You'll need to [install and configure the `wlc` client][4]*.

1. The `dev` branch (*upstream*) is moving. Developers do not
   `extract_messages` nor `update_catalog`.
1. From time to time, the person responsible for the translations updates
   weblate:
    1. Ensure weblate is in a clean state: all changes are commited (`wlc
       commit`).
    1. Block the translations on the component (`wlc lock
       rero_plus/<component>`).
    1. Push weblate on `rero:dev` (`wlc push rero_plus/<component>`).
    1. Pull the weblate commit locally (`git pull`).
    1. Extract the messages and update the catalogs. Commit the changes.
    1. Push *upstream* (`git push`).
    1. Verify that weblate is being automatically updated.
    1. Unlock translations on weblate (`wlc unlock rero_plus/<component>`).
1. Translators can work on weblate.
1. Weblate creates PR on the `dev` branch of the GitHub repository. 
1. Weblate PR are being merged into `dev`.

The section 2 could be scripted, once it's validated.

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





[1]: https://docs.weblate.org/en/latest/admin/continuous.html#automatically-receiving-changes-from-github
[2]: https://docs.weblate.org/en/latest/admin/continuous.html#avoiding-merge-conflicts
[3]: #the-regular-workflow
[4]: https://docs.weblate.org/en/latest/wlc.html
[5]: #some-weblate-settings
