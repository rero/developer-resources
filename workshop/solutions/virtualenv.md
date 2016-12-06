# Créer un environnement de travail

```bash
mkvirtualenv workshop1  # création du virtualenv
cdvirtualenv            # aller dans le rep. source
mkdir src               # création du répertoire
                        # installation de invenio-base
pip install -e git+https://github.com/inveniosoftware/invenio-base.git#egg=invenio-base
```