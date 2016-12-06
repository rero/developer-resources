# Charger une première donnée

```bash
                            # chargement du document
echo '{"album": "mon album préféré"}' | workshop1 records create --pid-minter recid
workshop1 index reindex     # mise dans la liste d'attente de tous les documents
workshop1 index run         # indexation
```

La donnée est visible avec ces urls:

- [http://localhost:5000/search](http://localhost:5000/search)
- [http://localhost:5000/api/records/1](http://localhost:5000/api/records/1)
- [http://localhost:5000/records/1](http://localhost:5000/records/1)