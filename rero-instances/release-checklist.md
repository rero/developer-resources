# Checklist for the release

This is mainly in the context of RERO ILS.

1. Make sure all the needed PRs are merged. Use the [RERO ILS PR project][1] and
   check with the dev team. If possible, check the relevant milestone.
1. Make sure the Github Actions tests were successful
1. Make sure the `staging` branches of the different projects have been carefully tested
   **with the [translations][3]**.
1. Check with the maintainers if the right version of `ng-core`
   (@jma) and `rero-ils-ui` (@jma) are published.
1. Follow [the workflow][2]:
    1. Check the [translations][3].
    1. Update the version numbers.
    1. The `CHANGES.md`.
    1. The `RELEASE-NOTES.rst`.
    1. Commit the changes.
    1. Tag the commit.
    1. Push on the upstream `master` branch.
    1. Publish the release (edit the tag).

After the release:

1. Ask a dev to update dependencies in each projects.
1. Ask a dev, in RERO and in UCLouvain to update the migration scripts.
1. Ask @rerowep, @BadrAly or @jma to deploy the published release on
   [ils.test.rero.ch][4].


[1]: https://github.com/orgs/rero/projects/5
[2]: release-publication.md
[3]: ../translations/translations-workflow.md
[4]: https://ils.test.rero.ch
