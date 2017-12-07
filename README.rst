========
ReducePy
========

.. image:: https://codecov.io/gh/abdullahselek/ReducePy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/abdullahselek/ReducePy
    :alt: Codecov

+---------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                Linux                                      |                                       Windows                                    |
+===========================================================================+==================================================================================+
| .. image:: https://travis-ci.org/abdullahselek/ReducePy.svg?branch=master | .. image:: https://ci.appveyor.com/api/projects/status/ngvmlb7lr7mf7k0n?svg=true |
|    :target: https://travis-ci.org/abdullahselek/ReducePy                  |    :target: https://ci.appveyor.com/project/abdullahselek/ReducePy               |
|    :alt: Travis-Ci                                                        |    :alt: AppVeyor                                                                |
+---------------------------------------------------------------------------+----------------------------------------------------------------------------------+

============
Introduction
============

Url shortener service using `Flask` and `Redis` runs on `Docker`.

================
Getting the code
================

The code is hosted at https://github.com/abdullahselek/ReducePy

Check out the latest development version anonymously with::

    $ git clone git://github.com/abdullahselek/ReducePy.git
    $ cd ReducePy

To install dependencies, run either::

    $ pip install -Ur requirements.testing.txt
    $ pip install -Ur requirements.txt

To install the minimal dependencies for production use run::

    $ pip install -Ur requirements.txt

=============
Running Tests
=============

The test suite can be run against a single Python version which requires ```pip install pytest``` and optionally ```pip install pytest-cov``` (these are included if you have installed dependencies from ```requirements.testing.txt```)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test -v --cov-report xml --cov=reducepy

To run the unit tests against a set of Python versions::

    $ tox

========
Commands
========

---
Run
---

Running up in Docker

.. code::

    docker-compose up

------------
Sample Usage
------------

.. code::

    # Shorten url with POST
    curl -i http://localhost:5000 -F "url=https://github.com"

    # Redirect to original url
    http://localhost:5000/YjUwYQ
