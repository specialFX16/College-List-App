import os, sys
path = 'var/www/CollegeList'
if path no in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'CollegeList.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
