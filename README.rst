==============
django-cluster
==============
Django-cluster is a framework for building microservice with Django.
Django-cluster will start up all the django projects in your cluster
and help you debug them.
Example:  You have a django project for your website.  You have several
other django projects that use django rest framework that act as an
API backend for your service and your website.  Instead of firing up
each of those django projects on different ports individually,
use django-cluster to runserver on them all for you and let it help you
debug them as they exchange http requests.

------------
Requirements
------------
Django

-------
Install
-------
Install package::

    pip install django-cluster

Note: do *not* install this in any of your projects' environments.
The cluster manager should be a project of it's own.

Add ``'lumberjack'`` to your ``INSTALLED_APPS``::

    # settings.py
    
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        'cluster',
    )

Create database tables::

    $ ./manage.py migrate lumberjack


-----
Usage
-----
TODO

