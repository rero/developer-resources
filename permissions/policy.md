# RERO ILS permissions policy

## Roles VS Policies

At first, RERO ILS used a custom permissions system based on user roles. Now, the
permissions use invenio-record-permissions' `Policy`.

- Allows more flexibility for managing/attributing permissions.
- Works with native `flask` notions (Permissions, Need).
- Will work in case of a migration to `invenio-record-resource`.

So, "librarian" and "system librarian" roles are replaced with multiple permissions:

- pro_read_only
- pro_acquisition_manager
- pro_catalog_manager
- pro_circulation_manager
- pro_library_administrator
- pro_user_manager
- pro_full_permissions

## Identity

A Flask application allows access to the `Identity` of the connected (or not) user. This `Identity` has an attribute (provides) that references a series of `Need` provided by this identity.

The permissions management via flask is based on the intersection between the `Need` requested by a `Permission` and the `Need` provided by an `Identity`. If the intersection of these 2 sets is not empty, then the permission is considered validated.

!!! So it is an **OR** condition that is used. There is no real way to play with **AND** conditions based on Flask permissions. There is no way to say that you need 2 `Needs` together.

When no user is logged in, the returned identity is 'AnonymousUser'. This identity has a special `Need`:

```python
from flask import g
print(g.identity)
>>> <AnonymousIdentity provides={
        Need(method='system_role', value='any_user')
    }>
```

Once the user is logged in, th identity has another `Need`:

```python
login_user(patron_martigny.user)
print(g.identity)
>>> <Identity id="1" provides={
        Need(method='system_role', value='any_user'),
        Need(method='system_role', value='authenticated_user'), 
        Need(method='id', value=1)
    }>
```

Thanks to flask's signals,we can add any `Need` subclass to this list:

```python
from flask_principal import identity_loaded, identity_changed

@identity_loaded.connect
def on_identity_loaded(sender, identity):
   user = load_custom_data(current_user)
   if user.has_blue_eyes:
        identity.provides.add(Need('eye-color', 'blue'))
   identity.provides.add(Need('age', user.age))
```

Invenio/flask already fills this Identiy with specific `Needs` related to the user's id and roles.

```python
..., Need(method='id', value=1), Need(method='role', value='patron')
```

## Policy

A `Policy` lists the actions that can be performed on a resource and who can perform them. The actions can be defined at will using the notation `can_<action_name>`. (we could have a permission, can_download, can_take_holiday, can_eat_candy, ...)

For each action, we define a list of `Generators` (Permissions) to specify who has access to this action.

Each `Generator`, can implement 3 methods :

- `needs()`: A list of needs allowing access to the resource.
  - if no `need` is returned -> access denied because the intersection between the `needs` of the permissions and the `needs` of the user == 0.
  - if at least one `need` of this list is provided to the identity of the connected user, it is valid. Condition **OR** !!!
- `exclude()`: a list of `needs` that deny access to the resource.
  - if only one of these `needs` is provided by the identity of the connected user, the Generator/permission will be denied. **The `exclude` always takes precedence over the `needs`!**
- `query_filter()` : TBD.

## ActionNeed and RoleActionAccess

Flask has a specific implementation of `Need` specific called `ActionNeed`.
Invenio proposes a mechanism that links a user role with an `ActionNeed` and a translation mechanism `ActionNeed` --> `RoleNeed|UserNeed`

The relationship between an action and a role/user is stored in DB in tables linked to the `invenio-access` module.
Thus, we can specify that **RoleA** has access to the **ReadRessourceX** action, that **User#1** does not have access to the **WriteRessourceY** action, ...

### Implementation in RERO ILS

- Each resource will have/implement 5 actions related to CRUD: search, get, create, update, delete.
- Each resource will have an implementation of a `Policy` that uses these actions to give access or not to this action.

### Yes, but what is `RestrictedByOrganization`?

Some actions should only be possible if the resource you want to update is in the same organization as the current_user... OK but how do we know that? Well, we use a `Need` !!!

```python
    def needs(self, record=None, *args, **kwargs):
        """Allows the given action filter by organisation.

        :param record: the record to check.
        :param kwargs: extra arguments.
        :returns: a list of Needs to validate access.
        """
        if record:
            # Check if the record organisation match an ``OrganisationNeed``
            required_need = OrganisationNeed(record.organisation_pid)
            if required_need not in g.identity.provides:
                return []
        return super().needs(record, **kwargs)
```

That's all well and good, but the identity doesn't provide any `OrganizationNeed`, so this permission will always fail (because it returns an empty array). Well, just add it to the identity!

## What about interactions with the UI

Nothing changes for the moment.
Permissions are currently checked using an API (`/permissions/<route_name>/[<ressource_pid>]`), this API doesn't change and returns exactly the same as before because it's still based on the permissions defined for each resource in the configuration file.

TODO: Document the UI interactions as implemented.

## Conclusion

We no longer restrict actions to roles but to actions. The actions that are linked to roles via a CLI command during `setup` (<https://github.com/zannkukai/rero-ils/blob/zan-organisation-permissions/rero_ils/modules/cli/fixtures.py#L81-L105>)

- The 'fine' management of permissions is facilitated.
- Customization of permissions would be possible (future US)
- 5 actions for each resource minimum.
- API operations are only restricted on actions and possibly filtered on an attribute of the record (organization, library, owner, ...)
- easy integration with `invenio-record-ressource`.
