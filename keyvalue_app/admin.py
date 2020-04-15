from django.contrib import admin

from . import models


admin.site.register(models.KeyValuePair)
admin.site.register(models.KeyFilePair)
