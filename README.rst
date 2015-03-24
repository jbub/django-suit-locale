django-suit-locale
==================

.. image:: https://pypip.in/v/django-suit-locale/badge.png?v109
    :target: https://pypi.python.org/pypi/django-suit-locale/

.. image:: https://pypip.in/d/django-suit-locale/badge.png?v109
    :target: https://pypi.python.org/pypi/django-suit-locale/

.. image:: https://pypip.in/wheel/django-suit-locale/badge.png?v109
    :target: https://pypi.python.org/pypi/django-suit-locale/

.. image:: https://pypip.in/license/django-suit-locale/badge.png?v109
    :target: https://pypi.python.org/pypi/django-suit-locale/

The aim of this project is to bring better localization process for Django Suit (http://djangosuit.com/).

What i have done
----------------

* generated suit locale files
* compared with ``django.contrib.admin`` locale files and removed duplicates
* compared with the supported packages and removed duplicates
* left the translations that do not maintain their own translation process
* left the translations that are from maintained packages but i did not found them

Package support
---------------

django-reversion
    Fork https://github.com/etianen/django-reversion and translate.

django-cms
    Translate at Transifex https://www.transifex.com/projects/p/django-cms/.

django-filer
    Translate at Transifex https://www.transifex.com/projects/p/django-filer/.

django-import-export
    This package is now translated, head over to https://github.com/bmihelac/django-import-export, fork and translate. I will keep the translations in this repository to give people some time to translate it. We will then remove the strings from this repository.

Localize
--------

Use Transifex to translate to your language https://www.transifex.com/projects/p/django-suit-locale/ or send a pull request with locale files.

Translators
-----------

* es - ernesto.ulloa
* fr - champsavoir
* ru - eu
* tr - erhansiraci
* pt_BR - mpena2099
* pl - dex4er
* sk, cs - jbub

Installation
------------

* Install easily using pip:

.. code-block:: bash

    pip install django-suit-locale

* Add ``suitlocale`` to your ``INSTALLED_APPS`` settings:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'suitlocale',
        'suit',
    )
