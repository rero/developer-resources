# State chart

:warning: See https://github.com/rero/rero-ils/blob/staging/doc/circulation/README.md

The circulation module follows 2 state charts: Item state chart and Loan state
chart. See below.

See also the [/data-graph-generation.md#circulation-policies][3] for graph
generation.

## Item state chart

- [PDF format][1]
- [The sources (graffle)][2]

# Implementation

It is implemented:

- into the `Class Item()` of `reroils-data/reroils_data/items/api.py` for the
  back end.
- into the `item.ts` file of the `reroils-circulation-ui` module for the front
  end.

# Data

You can generate a schema of circulation policies as explained here:
https://forge.o9.re/ODT/rero-ils-graphs/src/branch/master/by_json

It looks like:

![](https://framapic.org/QxE6G5vjmHMa/xWmXbcftw2EM)


[1]: https://github.com/rero/rero-ils/tree/dev/doc/circulation_statechart/circulation_item_statechart.pdf
[2]: https://github.com/rero/rero-ils/tree/dev/doc/circulation_statechart/circulation_item_statechart.graffle
[3]: data/data-graph-generation.md#circulation-policies
