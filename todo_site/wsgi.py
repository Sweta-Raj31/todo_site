"""
WSGI config for todo_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

project_home='/home/Sweta31/todo_site_'
if project_home not in sys.path:
    sys.path.insert(0,project_home)

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE']= 'deploy_on_pythonanywhere.settings'

application = get_wsgi_application()


