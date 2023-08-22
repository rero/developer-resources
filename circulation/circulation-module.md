# State chart

:warning: See [circulation documentation](https://github.com/rero/rero-ils/blob/staging/doc/circulation/README.md)

The circulation module follows two state charts: Item state chart and Loan state
chart. See below.

## Item state chart

- [PDF format][1]
- [The sources (graffle)][2]

### Implementation

It is implemented:

- into the `Class Item()` of `reroils-data/reroils_data/items/api.py` for the
  back end.
- into the `item.ts` file of the `reroils-circulation-ui` module for the front
  end.

[1]: https://github.com/rero/rero-ils/blob/staging/doc/circulation/circulation_item_statechart.pdf
[2]: https://github.com/rero/rero-ils/blob/staging/doc/circulation/circulation_item_statechart.graffle
