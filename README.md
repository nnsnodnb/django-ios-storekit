# django-ios-storekit

[![Build Status](https://travis-ci.org/nnsnodnb/django-ios-storekit.svg?branch=master)](https://travis-ci.org/nnsnodnb/django-ios-storekit)
[![Coverage Status](https://coveralls.io/repos/github/nnsnodnb/django-ios-storekit/badge.svg?branch=master)](https://coveralls.io/github/nnsnodnb/django-ios-storekit?branch=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-ios-storekit)
![PyPI](https://img.shields.io/pypi/v/django-ios-storekit)
![PyPI - Format](https://img.shields.io/pypi/format/django-ios-storekit)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/django-ios-storekit)

A Django plugin for iOS StoreKit server.

## Supported python versions

3.5.x ~ 3.7.x

## Supported django versions

2.0.x ~ 2.2.x

## Installation

```shell script
$ pip install django-ios-storekit
```

Add `storekit` into `INSTALLED_APPS` in `settings.py` file.

```python
INSTALLED_APPS += (
    'storekit',
)
```

```shell script
$ python manage.py migrate
```

## License

This software is licensed under the MIT License (See [LICENSE](https://github.com/nnsnodnb/django-ios-storekit/blob/master/LICENSE)).
