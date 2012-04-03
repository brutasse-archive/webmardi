How to play with this
---------------------

* Create a `virtualenv`_

  .. _virtualenv: http://pypi.python.org/pypi/virtualenv

* Install the requirements: ``pip install -r requirements.txt``

* Create an app on dev.twitter.com

* Create a minimal ``settings.py`` file in ``webmardi/settings.py``::

      from .default_settings import *

      DEBUG = True

      CONSUMER_KEY = 'your twitter app key'
      CONSUMER_SECRET = 'your twitter app secret'

      INTERNAL_IPS = ('127.0.0.1',)
      MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
          'debug_toolbar.middleware.DebugToolbarMiddleware',
      )

      INSTALLED_APPS += ('debug_toolbar',)

      DEBUG_TOOLBAR_CONFIG = {
          'INTERCEPT_REDIRECTS': False,
          'HIDE_DJANGO_SQL': False,
      }
* Create your database: ``python manage.py syncdb --noinput``

* Run the server: ``python manage.py runserver``

Admin
-----

Once you've logged in with your twitter account, you can add him admin
permissions: run this in ``python manage.py shell``::

    from django.contrib.auth.models import User

    u = User.objects.get(username='your twitter username')
    u.is_staff = True
    u.is_superuser = True
    u.save()

Now go to http://localhost:8000/admin/
