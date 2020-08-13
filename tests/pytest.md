# Py.Test

Python test suite. The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Installation

```bash
pip install pytest               # core
pip install pytest-cache         # bytest cache plugin
pip install pytest-cov           # generate code coverage report
pip install pytest-pep8          # check python code style
```

## Basics

### Write Tests

Put your tests in a directory named `tests`. Each name of files containing tests should starts with `test_`. Each test function should start with `test_`.

### Fixtures

### Files Hierarchy

```
my_project/
  my_module/
  tests/
  	 conftest.py                   # fixtures
    test_schemas.py
    test_cli.py
    test_model.py
  setup.py                        # python makefile
  pytest.ini                      # config file
```

### Run

```bash
py.test                           # run the test
py.test -s                        # run with stdout enable
py.test tests                     # run tests on the tests directory only
py.test tests/test_app.py         # run one file tests

```

## Configuration Files

### pytest.ini

```ini
[pytest]
addopts = --pep8 --ignore=docs --cov=simple_app --cov-report=term-missing
```

## References

1. [pytest](http://doc.pytest.org/)
