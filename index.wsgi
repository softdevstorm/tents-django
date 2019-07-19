import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/ubuntu/venv/lib/python3.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/html/tents-django')
#sys.path.append('/home/django_projects/MyProject/myproject')

os.environ['DJANGO_SETTINGS_MODULE'] = 'tents-django.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/ubuntu/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()