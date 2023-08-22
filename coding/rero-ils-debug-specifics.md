# RERO-ils debug specifics

In order to debug the RERO ILS API views and see tracebacks for your errors, uncomment `raise(error)` in `api_views.py` on lines:

* [68](https://github.com/rero/rero-ils/blob/bdaff2a54056b1aae7d9820993fa2883b88a038f/rero_ils/modules/items/api_views.py#L110)
* [110](https://github.com/rero/rero-ils/blob/bdaff2a54056b1aae7d9820993fa2883b88a038f/rero_ils/modules/items/api_views.py#L68)
