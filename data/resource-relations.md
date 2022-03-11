# Resource relations

:warning: See [`reroils_resources.svg`][1]

[1]: https://github.com/rero/rero-ils/blob/staging/doc/reroils_resources.svg

## Libraries

1. organisation *(required)*

## Locations

1. library *(required)*

## Items

1. organisations
1. locations *(required)*
1. documents *(required)*
1. holdings
1. item\_types *(required)*

## Loans

1. items
1. organisations

## Vendors

1. organisations *(required)*

## Circulation policies

1. organisations *(required)*
1. libraries
1. patron\_types
1. item\_types

## Patrons

1. patron\_types *(required for role: patron)*
1. libraries *(required for role: librarian and system_librarian)*

## Holdings

1. item\_types
1. locations
1. documents

## Patron\_transaction\_events

1. patron\_transactions
1. libraries *(required)*
1. patrons

## Acq\_accounts

1. budgets *(required)*
1. libraries *(required)*
1. organisations

## Acq\_orders

1. vendors *(required)*
1. libraries *(required)*
1. organisations

## Budgets

1. organisations

## Patron\_transactions

1. patrons *(required)*
1. notifications
1. organisations

## Notifications

1. loans *(required)*

## Acq\_order\_lines

1. acq\_accounts *(required)*
1. acq\_orders
1. documents *(required)*
1. organisations
