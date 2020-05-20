# Imports

Python imports can be reorganized, sorted, and changed during development.

Here are some best practices about Python imports.

## Sort imports

```bash
poetry run isort -rc rero_ils tests
```

## Remove unused imports

```bash
poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r .
```

## Tip: create an alias to sort imports and remove unused imports

Add a new line in your **.bashrc** or **.zshrc**:

```bash
alias fixsort="poetry run isort -rc rero_ils tests && poetry run autoflake --remove-all-unused-imports -i --ignore-init-module-imports -r ."
```