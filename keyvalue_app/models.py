from django.db import models


class KeyValuePair(models.Model):
    key = models.TextField()

class KeyFilePair(models.Model):
    key = models.FileField(upload_to='keys')

