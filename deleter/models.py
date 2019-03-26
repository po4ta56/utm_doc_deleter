from django.db import models


class Document(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=255)
    is_incoming = models.BooleanField()