from django.db import models


class DocumentInboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    
    
class DocumentOutboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)