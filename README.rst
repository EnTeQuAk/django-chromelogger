
.. image:: https://badge.fury.io/py/django_chromelogger.svg
   :target: https://pypi.python.org/pypi/django_chromelogger

.. image:: https://travis-ci.org/EnTeQuAk/django-chromelogger.svg?branch=master
   :target: https://travis-ci.org/EnTeQuAk/django-chromelogger


====================
Django Chrome Logger
====================

Chrome-Logger_ support for Django. ChromeLogger is a protocol which allows sending logging messages to the Browser.

This module implements simple support for Django. It consists of two components:

* `LoggingMiddleware` which is responsible for sending all log messages associated with the request to the browser.
* `ChromeLoggerHandler` a python logging handler which collects all messages.

.. hint::

    The documentation and library is still work in progress. Please use at your own risk.


Configuration in settings.py is as follows:

.. code-block:: python

    MIDDLEWARE = [
        'chromelogger.LoggingMiddleware',
        ... # other middlewares
    ]

    LOGGING = {
        ...
        'handlers': {
            'browser': {
                'class': 'chromelogger.ChromeLoggerHandler',
            },
            ...
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'browser'],
                'level': 'DEBUG',
            },
            ...
        }
    }


The code lives on GitHub_, where you can report Issues_. The full
documentation is available on ReadTheDocs_.


.. _Chrome-Logger: https://craig.is/writing/chrome-logger
.. _GitHub: https://github.com/EnTeQuAk/django-chromelogger
.. _Issues: https://github.com/EnTeQuAk/django-chromelogger/issues
.. _ReadTheDocs: http://django-chromelogger.readthedocs.org/
