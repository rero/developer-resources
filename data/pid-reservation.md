# PID Reservation

To reserve a range of pids for future records loading,
reserved pids will have the status `RESERVED`.

For information on how to use the new cli:

```bash
pipenv run invenio utils reserve_pid_range --help
```

Available options:

```bash
    - pid_type: the pid type of the resource as configured in config.py,
      - example: itm for the item resource
    - records_number: number of new records(with pids) to load.
    - unused: set that the status of unused (gaps) pids to NEW. 
```

Call examples:

To reserve 100 pids for `patrons` loading:

```bash
pipenv run invenio utils reserve_pid_range -p ptrn -n 100
```

To:

- reserve 2 pids for `organisations` loading and
- fill the gap of the unused pids and assign the status `NEW`to them

```bash
pipenv run invenio utils reserve_pid_range -p org -n 2 -u
```
