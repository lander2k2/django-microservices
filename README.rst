====================
django-microservices
====================
Django-microservices helps you manage the development and interaction
of microservices built in Django.

--------
Use Case
--------
You are using Django to build an application with a microservices architecture.
You have serveral services that communicate to each over HTTP and each service
is it's own Django project.  You need to run `./manage.py runserver [port]` for
each service to bring it up and have the application function when developing.

Django-microservices helps by:
#. giving you a single `/.manage.py runcluster` command to fire up the development
   server for each project
#. providing a service discovery API that will allow your services to find one another

------------
Requirements
------------
Django

-------
Install
-------
Create a *new* virutual environment and django project alongside the django
projects that make up your micoservices application::
    
    $ mkvirutalenv myapp_service_manager
    $ pip install django django-microservices psycopg2 # for postgres database
    $ django-admin startproject service_manager
    $ cd service_manager

Create your service manager database::

    $ createdb myapp_service_manager  # if using postgres

Edit the settings in your new service manager project.  Add ``microservices``
to the ``INSTALLED_APPS`` add the database settings::

    # service_manager/settings.py
    
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        'microservices',
    )

    # for postgres database
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'myapp_service_manager',
            'USER':     'db_user',
            'PASSWORD': 'secret',
            'HOST':     'localhost',
            'PORT':     '5432',
        }
    }
    
Create database tables::

    $ ./manage.py migrate

Create an admin user::

    $ ./manage.py createsuperuser

Edit the root urls file to look like this::

    # service_manager/urls.py

    from django.conf.urls import include, url
    from django.contrib import admin

    from microservices.admin import services_admin_site

    urlpatterns = [
        url(r'^',      include('microservices.urls')),
        url(r'^admin/', include(services_admin_site.urls)),
    ]


-----
Usage
-----

In your service manager project, run `./manage.py runcluster` then navigate
to `http://127.0.0.1:8000`.

The first time you do this, you won't see any services registerd.  Click
on the "Admin" link, log in and register services by clicking on "Services"
in the Microservices admin.  Click "Add service" to add each new service
in your app.

Now at the index page of the service manager project you will see a list of 
services with links to each.

For any application that needs to find services in the cluster, add this to
the settings.py file::

    import requests

    SERVICES = requests.get('http://127.0.0.1:8000/services/').json()

Then use `settings.SERVICES[service_name]` to get the correct IP for any service
in your application.

