# How to add a new language

:warning: This guide is not valid anymore. It should be updated!

This guide is tested for RERO-ILS v0.5.2

### Step 1 : translations for RERO-ILS
install language file from transifex (rero-ils project) :
```sh
$ pipenv run tx pull -l es #es for spanish
```
### Step 2 : translations for UI
install language file from transifex (rero-ils-ui project) :
```sh
$ cd  ui
$ pipenv run tx pull -l es #es for spanish
```

### Step 3 : configure languages
Update I18N_LANGUAGES variable in `config.py` to add the new language :

e.g. for spanish :
```python
I18N_LANGUAGES = [
    ('fr', _('French')),
    ('de', _('German')),
    ('it', _('Italian')),
    ('es', _('Spanish')),
]
```

Define the new language in manual translation file to add `ui_language_<language>`:

e.g. :
```
# Menu language
_('ui_language_en')
_('ui_language_fr')
_('ui_language_de')
_('ui_language_it')
_('ui_language_es')
```

For each existing languages, add the new translation in:

`rero-ils/translations/<language>/LC_MESSAGES/messages.po`

e.g. :
```
#: rero_ils/manual_translations.txt:64
msgid "ui_language_es"
msgstr "Español"
````

### Step 4 : bootstrap project
Finally, run bootstrap to rebuild UI and assets:
```sh
$ ./script/bootstrap
```
