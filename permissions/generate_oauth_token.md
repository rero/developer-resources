# How to generate an Oauth token for reroils users

You can now create a personalized access token for RERO ILS users.

Currently, the access token is used for posting MARCXML documents via
the document API only (in testing by NGSCAN/EZPUMP)

To generate an access token for a user:

```bash

poetry run invenio utils tokens_create -n name -u reroilstest@gmail.com
```

To generate pass an access token to a user:

```bash

poetry run invenio utils tokens_create -n name -u reroilstest@gmail.com -t access_token
```
