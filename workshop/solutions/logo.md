# Changer le logo

```bash
mkdir -p workshop1/static/images
wget "https://gitlab.rero.ch/rero-projects/invenio-survival-guide/raw/master/workshop/data/logo.png" -O workshop1/static/images/logo.png
workshop1 collect -v
echo "THEME_LOGO='images/logo.png'" >> workshop1/config.py
```

__Note__: ne pas oublier d'exécuter `my_instance collect` pour que l'image soit déployée.