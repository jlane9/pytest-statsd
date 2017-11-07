pytest-statsd
=============

[![Build Status](https://travis-ci.org/jlane9/pytest-statsd.svg?branch=master)](https://travis-ci.org/jlane9/pytest-statsd)
[![PyPI version](https://badge.fury.io/py/pytest-statsd.svg)](https://badge.fury.io/py/pytest-statsd)
[![Python version](https://img.shields.io/pypi/pyversions/pytest-statsd.svg)](https://pypi.python.org/pypi/pytest-statsd)
[![License](https://img.shields.io/pypi/l/pytest-statsd.svg)](https://pypi.python.org/pypi/pytest-statsd)
[![Status](https://img.shields.io/pypi/status/pytest-statsd.svg)](https://pypi.python.org/pypi/pytest-statsd)
[![Requirements Status](https://requires.io/github/jlane9/pytest-statsd/requirements.svg?branch=master)](https://requires.io/github/jlane9/pytest-statsd/requirements/?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pytest-statsd/badge/?version=latest)](http://pytest-statsd.readthedocs.io/en/latest/?badge=latest)
[![Maintainability](https://api.codeclimate.com/v1/badges/c43f457e5826cedcf08f/maintainability)](https://codeclimate.com/github/jlane9/pytest-statsd/maintainability)


Installation
------------

Install through pip:

```bash
pip install pytest-statsd
```


Install from source:

```bash

cd /path/to/source/pytest-statsd
python setup.py install
```

Example
-------

To simply run using default the configuration, use:

```bash
pytest --stats-d tests/
```


If there is a need to configure where to sent results to other than localhost:8125, use:

```bash
pytest --stats-d --stats-host http://myserver.com --stats-port 3000 tests/
```

You can also prefix your results if you plan on having multiple projects sending results to the same server:

```bash
pytest --stats-d --stats-prefix myproject test/
```