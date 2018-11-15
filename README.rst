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

Url shortener service using `Tornado` and `Redis` runs on `Docker` and `Kubernetes`.

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
    
========================    
Downloading Docker Image
========================

You can download docker image with::

    docker pull abdullahselek/reducepy
    
and the docker page for the image https://hub.docker.com/r/abdullahselek/reducepy/.

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

Running in Kubernetes

- For testing you can run **reducepy** in **Kubernetes** with using **Docker**. Run docker and then the following
commands should work for you.

.. code::

    # Use Docker for minikube
    eval $(minikube docker-env)

    # Create developments and pods
    kubectl create -f deployment-redis.yml
    kubectl create -f deployment-reducepy.yml

    # Create services
    kubectl create -f service-redis.yml
    kubectl create -f service-reducepy.yml

    # Get url for **reducepy**
    minikube service reducepy --url

------------
Sample Usage
------------

.. code::

    # Shorten url with POST
    curl -i http://127.0.0.1 -F "url=https://github.com"

    # Response
    {
        "error": false,
        "shortened_url": "http://127.0.0.1/YjUwYQ"
    }

    # Redirect to original url
    http://127.0.0.1/YjUwYQ

    # Error case with invalid url
    curl -i http://127.0.0.1 -F "url=github"

    # Response
    {
        "error": true,
        "message": "Please post a valid url"
    }

    # Error case with null url
    curl -i http://127.0.0.1 -F "url="

    # Response
    {
        "error": true,
        "message": "Please post a url"
    }
