# Recommendations

Some coding recommendations specific to RERO+ projects.

## Python typing

Introduced since Python `3.5`, [typing](https://docs.python.org/fr/3.10/library/typing.html)
allows to specify types for variables or functions. For RERO+ projects, this
feature is not recommended, since it doesn't add any value to the code.

## Data serialization

Exporting long lists of results from an ES query implies using `scan()` instead
of `execute()`. `execute()` uses `invenio-record-rest` but not `scan()`. This
means that we have to duplicate code when using `scan()`.

- As of 2022-07, we keep using `invenio-record-rest`. When we need to stream an
export with `scan()`, we use a specific mounting point.
- Long-term, we can begin to migrate some resources to `Invenio resources`,
which is more flexible and allows class supercharging.
- To avoid high server loads, limit the number of results for each export with
a config variable. Above this limit, streaming is not allowed and requires an
external task.
- `scan()` can create ElasticSearch timeouts. Each export task should be
possible with a CLI that avoids any nginx or ES timeout.

## Prettyfier

Recommended code prettyfier plugins:

- Python: *to be determined*
- Typescript/Angular: *to be determined*

**Note:** Cosmetic suggestions in code reviews should be identified as such, and
can be ignored by the author of the original code.