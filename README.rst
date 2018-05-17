django-ios-storekit
===================

.. image:: https://travis-ci.org/nnsnodnb/django-ios-storekit.svg?branch=travis
    :target: https://travis-ci.org/nnsnodnb/django-ios-storekit
.. image:: https://coveralls.io/repos/github/nnsnodnb/django-ios-storekit/badge.svg?branch=travis
    :target: https://coveralls.io/github/nnsnodnb/django-ios-storekit?branch=travis

A Django plugin for iOS StoreKit server.

Supported python versions
-------------------------

2.7, 3.4, 3.5, 3.6

Supported django versions
-------------------------

1.7 - 1.11, 2.0(only Python3.4 or later)

Installation
------------

.. code:: bash

    $ pip install django-ios-storekit

Add ``storekit`` into `INSTALLED_APPS` in ``settings.py`` file.

.. code:: python

    INSTALLED_APPS += (
        'storekit',
    )

Author
------

nnsnodnb

LICENSE
-------

Copyright (c) 2017 Yuya Oka Released under the MIT license (see `LICENSE <LICENSE>`__)

