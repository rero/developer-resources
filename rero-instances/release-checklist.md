# Checklist for the release

This is mainly in the context of RERO ILS.

1. Make sure all the needed PR are merged. Use the [RERO ILS PR project][1] and
   check with the dev team.
1. Check with the maintainers if the right version of `ng-core`
   (@sebastiendeleze) and `rero-ils-ui` (@jma) are published.
1. Follow [the workflow][2]: checks the translations, update the version
   numbers, the changelog, release notes, commit the changes, tag the commit,
   publish the release.

After the release:

1. Ask a dev to update dependencies in each projects.
1. Ask a dev, in RERO and in UCLouvain to update the migration scripts.


[1]: https://github.com/orgs/rero/projects/5
