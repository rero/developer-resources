# Création et installation de la nouvelle instance `invenio`

## Création et installation

```bash
cdvirtualenv src        # aller dans le rep. source
                        # création de l'instance
inveniomanage instance create workshop1
cd workshop1            # aller dans le projet
                        # installation des paquets d'invenio
pip install -r requirements-devel.txt
pip install -e .        # installation de l'instance
```

## Docker

__Dans un nouveau terminal!__

```bash
workon workshop1           # pour avoir les commandes virtualenv
cdvirtualenv src/workshop1 # retour dans le répertoire de travail
                           # création du fichier docker
echo '
elasticsearch:
  image: elasticsearch:2.4
  ports:
    - "9200:9200"
    - "9300:9300"

redis:
  image: redis
  ports:
    - "6379:6379"

rabbitmq:
  image: rabbitmq:3-management
  ports:
    - "5672:5672"
    - "15672:15672"
' > docker-compose.yml

docker-compose up        # lancement des services
```

## Installation des fichiers statiques et `css` et `js`

```bash
workshop1 npm           # création de la liste des dep. nodejs
workshop1 collect -v    # collecte des fichiers statiques
cd ../../var/workshop1-instance/static
npm i                   # installation des dépendences nodejs
                        # installation des outils pour les assets
npm install -g --prefix ${VIRTUAL_ENV} node-sass@3.8.0 clean-css requirejs uglify-js
workshop1 assets build  # assets


workshop1 run            # lancement serveur développement
```

## Erreur dans la page de résultats

La page de résultat contient une erreur car la base de donnée et l'indexation ne sont pas initialisés.