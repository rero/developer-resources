# SQL Migrations

## Add property to metadata

The following query will add the `myProperty` property to JSON metadata for all documents. With the last argument of the `jsonb_set` function allows to create the property if it does not exist.

```sql
UPDATE records_metadata SET json = jsonb_set(json, '{myProperty}', 'false', true) 
````

## Remove property from metadata

This statement removes the `myProperty` property from all records. It does not generate an error if the property does not exist.

```sql
UPDATE records_metadata SET json = json - 'myProperty'
```
