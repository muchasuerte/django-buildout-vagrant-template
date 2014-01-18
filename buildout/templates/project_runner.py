import os

from django.conf import ENVIRONMENT_VARIABLE
os.environ[ENVIRONMENT_VARIABLE] = '${django:project}.${django:settings}'
from django.conf import settings

from django.core.handlers.wsgi import WSGIHandler
from django.views import debug
from django_extensions.management.commands.runserver_plus import null_technical_500_response
from werkzeug import DebuggedApplication

debug.technical_500_response = null_technical_500_response

if settings.DEBUG:
    application = DebuggedApplication(WSGIHandler(), True)
else:
    application = WSGIHandler()
