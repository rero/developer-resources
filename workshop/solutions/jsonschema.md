# Validation des données avec JSON-Schema

## Chargement des données avec validation
Cette commande va échouer car il existe des titres d'album de moins de 3 caractères. Il faut modifier la propriété `minLength` (valeur à 1 par ex.) pour le champ `album` dans le fichier `workshop1/schemas/records/record-v1.0.0.json`.
```bash
cat data/data.json| dojson -i - schema "http://workshop.rero.ch/schemas/records/record-v1.0.0.json" | workshop1 records create --pid-minter recid
```