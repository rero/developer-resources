# Workshop 1

Ce workshop a pour but de créer une instance `invenio` de zéro, de charger des données et d'adapter l'interface utilisateur. Il utilise les notions vues précédemment, mais ne nécessite pas une connaissance importante du langage `python`.

__prérequis__:

- pouvoir créer un environnement virtuel python (testé avec 3.5.2)
- pouvoir exécuter les outils docker: `docker-compose`
- avoir `nodejs` installé: la commande `npm` doit exister
- avoir `git` installé

### Table des matières

#### [1. Etape 1: créer une nouvelle instance](#etape-1-cr-er-une-nouvelle-instance)
- [L'environnement de travail](#l-environnement-de-travail)
- [Une nouvelle instance invenio](#une-nouvelle-instance-invenio)
- [Initialiser l'application](#initialiser-l-application)

#### [2. Etape 2: les données](#etape-2-les-donn-es)
- [Charger une première donnée](#charger-une-premi-re-donn-e)
- [Validation de données avec JSON-Schema](#validation-de-donn-es-avec-json-schema)
- [Navigation par facettes](#navigation-par-facettes)

#### [3. Etape 3: l'interface utilisateur](#etape-3-l-interface-utilisateur)
- [Changer le logo](#changer-le-logo)
- [Ajustement la présentation des résultats](#ajustement-la-pr-sentation-des-r-sultats)
- [Correction la présentation des facettes](#correction-la-pr-sentation-des-facettes)

#### [4. Conclusion](#conclusion)
#### [5. Références](#r-f-rences)

----------------
## Etape 1: créer une nouvelle instance

### But

Créer une nouvelle instance `invenio` simple basée sur `sqlite` et qui répond à l’adresse: http://localhost:5000. Cette instance devra être installée dans un environnement virtuel `python` et utilisera `docker` pour les services externes (par ex. `Elasticsearch`). Nous utiliserons l'outil fournit par `invenio`: `inveniomanage` compris dans le paquet `invenio-base`.

### Astuce

Une instance `invenio` est un paquet python comprenant le fichier de configuration `config.py`, ainsi que les outils soit pour lancer un site web de développement `python` soit pour le déployer via `apache` ou `nginx`.

### L'environnement de travail

#### But

Nous voulons utiliser les outils `invenio` pour créer une nouvelle instance. Pour faire les choses proprement, nous allons créer un environnement virtuel pour notre nouvelle instance.

#### Commandes utiles

##### virtualenv:

```bash
mkvirtualenv workshop1  # création d'un environnement virtuel
cdvirtualenv            # aller dans le répertoire de travail
deactivate              # sortir de l'environnement virtuel
```

##### python

```bash
pip install Flask   # installer un paquet par ex. Flask
pip install .       # installer un paquet depuis le répertoire contenant `setup.py`
pip install -e  xxx # installer en conservant les sources
                    # installer un paquet depuis github
pip install git+https://github.com/inveniosoftware/invenio-xx.git#egg=invenio-xx
```

#### Exercice

1. créer un environnement virtuel python nommé `workshop1`
2. créer un répertoire `src` dans le virtualenv
3. installer `invenio-base` (version github) dans le répertoire `src`

Si tout s'est bien passé vous avez une nouvelle commande disponible: `inveniomanage` et les sources de ce paquet installé dans `src`. Vous pouvez dès à présent explorer la commande pour créer la nouvelle instance.

__[La Solution](solutions/virtualenv.md#cr-er-un-environnement-de-travail)__

#### Discussion

C'est une bonne pratique d'installer les paquets python et les sources du projet dans le répertoire de l'environnement virtuel. Ceci permet de lier naturellement les sources et l'environnement de développement. Attention toutefois à bien sauvegarder vos modifications (`git push`) avant de détruire l'environnement virtuel.

### Une nouvelle instance `invenio`

#### But

Créer et installer la nouvelle instance.

#### Commandes utiles

##### python

```bash
pip install -r list.txt   # installer une liste de paquets depuis un fichier
pip install -e .          # installer en dev un paquet depuis un répertoire contenant setup.py
```
 __note__: l'option `-e` crée des liens symboliques au lieu d'une copie lors de l'installation du paquet. Ceci évite la réinstallation du paquet lors de la modification des sources.

##### Flask

Pour lancer le serveur web avec un rechargement automatique lors des modifications des fichiers:

```bash
# debug mode (chargement automatique lors de la modification des sources)
export FLASK_DEBUG=1

my_instance run
```

##### Docker

```bash
docker-compose build  # création des images docker
docker-compose up     # exécution des containers
docker-compose down   # arrêt des containers avec perte des données
```

##### nodejs

__note__: il existe un équivalent à `pyenv` dans le monde de `nodejs`: `nvm` (https://github.com/creationix/nvm#install-script).

```bash
# installation des outils nodejs utilisé par Invenio
npm install -g --prefix ${VIRTUAL_ENV} node-sass@3.8.0 clean-css requirejs uglify-js
npm install   # installation des paquets nodejs décrits dans packages.json
```
__note__: `nodejs` est utilisé pour le code `javascript` de l'interface utilisateur. Les paquets `js` d'invenio suivent la dénomination `invenio-xxx-js`.

##### invenio

```bash
inveniomanage instance create xxx  # création d'une nouvelle instance

my_instance npm                    # création de la liste des dépendences js
my_instance collect                # collecte des fichiers statiques
my_instance assets build           # compilation des fichiers js et css
```
__note__: my_instance est à remplacer par le nom de l'instance ici `workshop1`. Ceci permet l'interaction avec différentes instances sur la même machine.

#### Exercice

1. créer la nouvelle instance avec l'outil fournit avec `invenio-base` dans le répertoire `src` nouvellement créé
2. explorer les fichiers créés et identifier les fichiers utiles pour la suite de l'installation
3. installer les paquets python utilisé pour le développement
4. installer l'instance elle-même
5. installer les dépendances `nodejs`, les fichiers statiques et les assets (`css` et `js`)
6. installer et exécuter les services `dockers`
7. lancer le serveur de développement et visualiser l'application `http://localhost:5000`

A cette étape le serveur répond à [http://localhost:5000](http://localhost:5000).

__[La Solution](solutions/install.md#cr-ation-et-installation-de-la-nouvelle-instance-invenio)__


### Initialiser l'application

#### But

Initialiser les services: base de donnée et indexation.

#### Commandes utiles

##### invenio

```bash
my_instance db --help            # utilitaire de base de données
my_instance index --help         # utilitaire pour l'indexation
my_instance index queue --help   # utilitaires de queue d'indexation
```

#### Exercice

1. initialiser la base de donnée
2. initialiser le moteur d'indexation
3. obtenir "no results" pour [http://localhost:5000/search](http://localhost:5000/search)

__[La Solution](solutions/init.md#initialiser-l-application)__

#### Discussion

A présent l'instance est installée. Elle ne contient aucune donnée. C'est le début de sa personnalisation.

----------------
## Etape 2: les données

### But

Se familiariser avec les données au format `JSON` et leur chargement dans le système soit une par une soit par lots. Il faudra les valider avec `jsonschema` et configurer le moteur de recherche.

### Astuces

#### Elasticsearch

- [voir les indexes](http://localhost:9200/_alias?pretty=true)
- [voir les données indexées](http://localhost:9200/records/_search?pretty=true)
- [voir le mapping de l'index records](http://localhost:9200/records/_mapping?pretty=true)

### Charger une première donnée

#### But

Créer une nouvelle donnée, la stocker dans la base de donnée et l'indexer. Nous voulons aussi avoir des identifiants pérennes: pid's (rappelez-vous la notion de minter). Nous utiliserons un scénario de création d'un catalogue d'albums de musique.

#### Commandes utiles

```bash
my_instance records --help    # utilitaire de données
my_instance index --help      # utilitaire d'indexation
```

#### Exercice

1. charger un nouveau document dans la base une donnée avec un champ `album=mon album préféré`. __Note:__ ne pas oublier les identifiants (minter)!
2. indexer le document
3. visualiser la donnée dans la page des résultats, la vue détaillée et l'API REST

__[La Solution](solutions/simple_data.md#charger-une-premi-re-donn-e)__

#### Discussion

La commande `workshop1 index reindex` ne lance pas l'indexation! Elle ne fait que la mettre dans la queue.

### Validation de données avec JSON-Schema

#### But

Créer et installer un `schema` correspondant à nos données. Cela nous permettra de nous familiariser avec la validation de données.

#### Commandes utiles

```bash
dojson --help    # utilitaire de données
```

#### Préparation

Il faut installer un nouveau schéma dans l'instance et copier le fichier `JSON` comprenant les données:

```bash
mkdir -p workshop1/schemas/records
touch workshop1/schemas/records/__init__.py
touch workshop1/schemas/__init__.py
wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/schemas/record-v1.0.0.json" -O workshop1/schemas/records/record-v1.0.0.json

# ajouter les lignes suivantes au entrypoints de `setup.py`
# 'invenio_jsonschemas.schemas': [
#   'records = workshop1.schemas'
#  ]

pip install -e .  # déclaration du schéma local à invenio-jsonschemas

echo "
# invenio-jsonschemas
JSONSCHEMAS_HOST = 'workshop.rero.ch'
" >> workshop1/config.py

mkdir data
wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/data.json" -O data/data.json
```

__Vérification:__ le schema doit exister via [http://localhost:5000/schemas/records/record-v1.0.0.json](http://localhost:5000/schemas/records/record-v1.0.0.json).

__Note:__ à chaque fois que le fichier `setup.py` est modifié il faut réinstaller l'instance.

#### Exercice

1. examiner et charger les données `data/data.json` en rajoutant le schema avec l'aide de `dojson`
2. corriger le schema au besoin

__[La Solution](solutions/jsonschema.md#validation-des-donn-es-avec-json-schema)__


### Navigation par facettes

#### But

Configuration de la navigation par facettes.

#### Préparation

Nous allons récupérer une configuration de base pour les facettes (fichier: `workshop1/config.py`) et installer un mapping `elasticsearch`.

```bash
wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/config_facets.py" -O workshop1/config.py
mkdir -p workshop1/mappings/records/
touch workshop1/mappings/records/__init__.py
touch workshop1/mappings/__init__.py

wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/mapping/record-v1.0.0.json" -O  workshop1/mappings/records/record-v1.0.0.json
# ajouter les lignes suivantes aux entrypoints de `setup.py`
#  'invenio_search.mappings' : [
#    'records = workshop1.mappings'
#  ]
pip install -e .
```
__Note:__ il arrive fréquemment d'oublier la création des fichiers `__init__.py`: ils sont nécessaires à `python` pour que celui-ci considère un répertoire comme un paquet. Ils ne sont par exemple pas nécessaire dans les répertoires `static` car ceux-ci ne sont utilisés que pour la partie interface utilisateur (`javascript`, `css`).

#### Exercice

1. ré-indexer les données avec le nouveau `mapping`
2. visualiser les facettes
3. rajouter la facette `artist` et modifier le mapping `Elasticsearch` au besoin

__[La Solution](solutions/facets.md#navigation-par-facettes)__

#### Discussion

Lorsque le `mapping` est touché, il est nécessaire de ré-indexer. Ceci peut paraître lourd, mais c'est inévitable. Par chance, `Elasticsearch` permet de créer et remplir un nouvel index tout en utilisant l'ancien; il sera part contre nécessaire de rattraper les notices touchées durant le processus. Le mécanisme d'`alias` permet la commutation d'indexes à chaud.


----------------
## Etape 3: l'interface utilisateur

### But

Adapter et personnaliser l'interface utilisateur au schema de nos données.

### Changer le logo

#### But

Remplacer le logo `invenio` contenu dans l'entête du site.

#### Commandes utiles

```bash
my_instance collect    # récolte les fichiers statiques
```

#### Exercice

1. Créer les répertoires `static/images` dans l'instance
2. Copier le logo [https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/logo.png](https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/logo.png) dans le répertoire crée
3. Ajouter le logo au site (variable `THEME_LOGO`)

__[La Solution](solutions/logo.md#changer-le-logo)__

#### Discussion

A chaque fois que des fichiers sont rajoutés dans le répertoire `static` il est nécessaire d'exécuter la commande `collect`. Ils seront installé dans le répertoire de l'instance (variable `instance_path` d'une application `Flask`). Dans notre cas: '../../var/workshop1-instance'.

### Ajustement la présentation des résultats

#### But

La liste des résultats n'affichent pas correctement les champs de la notice. Il faut donc modifier les `templates` d'`angularjs` pour l'adapter à nos données. Nous allons afficher le titre de l'album, le nom de l'artiste et la liste des musiciens.

#### Astuces

L'API REST permet de voir des exemples de notices:

- [http://localhost:5000/api/records](http://localhost:5000/api/records): affiche une liste résultats
- [http://localhost:5000/api/records/1](http://localhost:5000/api/records/1): affiche la première notice
- la syntaxe dans un template `angularjs` pour afficher le contenu d'une variable est `{{ variable_name }}`

__note:__ lorsque l'on change une variable, il faut cocher `Disable cache` dans les outils de développement du navigateur.

#### Préparation

```bash
# copier un exemple de template
mkdir -p workshop1/static/templates/workshop1
wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/record_brief.html" -O workshop1/static/templates/workshop1/record_brief.html

# collecte le nouveau fichier statique
workshop1 collect -v

# change le template des résultats
echo "SEARCH_UI_JSTEMPLATE_RESULTS = \
    'templates/workshop1/record_brief.html'" >> workshop1/config.py
```

#### Exercice

1. Modifier le fichier de `template` pour afficher les différents champs de la notice

__[La Solution](solutions/detailed_view.md#ajustement-de-la-pr-sentation-des-r-sultats)__

#### Discussion

Lorsque l'interface utilisateur demande une grande interaction avec l'utilisateur `angularjs` est utilisé, sinon c'est le couple `Flask` - `Jinja` qui s'en charge. Il peut-être déroutant d'avoir deux langages de `template` et il est souvent nécessaire de visiter les paquets pour savoir quelle technologie est utilisée. Lorsque les templates sont dans le répertoire `static` alors c'est certainement une application `angularjs`.

### Correction la présentation des facettes

#### But

Un bug est présent dans le `template` des facettes; en effet la facette année est présente deux fois. Une fois sous forme de graphique et une fois sous forme textuelle. Il faut supprimer cette dernière.

#### Astuces

S’inspirer du point précédent pour installer le template des facettes contenu dans le module `nodejs`: `invenio-search-js`.

#### Exercice

1. installer un fichier de template pour les facettes, par ex. en reprenant celui d'`invenio-search-js`
2. ajouter la configuration
3. modifier le fichier de template pour ne pas afficher la facette `years`

__[La Solution](solutions/facets_view.md##ajustement-la-pr-sentation-de-la-facette)__

## Conclusion

Nous voici au terme de ce workshop. Vous avez créé une instance de zéro et chargé vos propres données. Gardez ce tutoriel sous la main cela vous sera certainement utile dans le futur!

## Références

1. [nvm](https://github.com/creationix/nvm)
2. [invenio-base](https://github.com/inveniosoftware/invenio-base)
3. [invenio sur github](https://github.com/inveniosoftware)
4. [invenio](http://invenio-software.org)
5. [docker](https://www.docker.com/)
6. [Elasticsearch](https://www.elastic.co/)
7. [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)