django-ios-storekit
===================

.. image:: https://travis-ci.org/nnsnodnb/django-ios-storekit.svg?branch=travis
    :target: https://travis-ci.org/nnsnodnb/django-ios-storekit
.. image:: https://coveralls.io/repos/github/nnsnodnb/django-ios-storekit/badge.svg?branch=travis
    :target: https://coveralls.io/github/nnsnodnb/django-ios-storekit?branch=travis
.. image:: https://img.shields.io/pypi/pyversions/django-ios-storekit
.. image:: https://img.shields.io/pypi/v/django-ios-storekit
.. image:: https://img.shields.io/pypi/format/django-ios-storekit
.. image:: https://img.shields.io/pypi/wheel/django-ios-storekit

A Django plugin for iOS StoreKit server.

Supported python versions
-------------------------

3.5.x ~ 3.7.x

Supported django versions
-------------------------

2.0.x ~ 2.2.x

Installation
------------

.. code:: bash

    $ pip install django-ios-storekit

Add ``storekit`` into `INSTALLED_APPS` in ``settings.py`` file.

.. code:: python

    INSTALLED_APPS += (
        'storekit',
    )

.. code:: bash

    $ python manage.py migrate

Author
------

nnsnodnb

LICENSE
-------

Copyright (c) 2017 Yuya Oka Released under the MIT license (see `LICENSE <LICENSE>`__)

