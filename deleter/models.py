from django.db import models

import requests



class DocumentInboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    text = models.TextField()
    
    class Meta:
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящие документы'       

    
class DocumentOutboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    text = models.TextField()

    class Meta:
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'
        ordering = ('-title',) # сортировка по умолчанию в обратном порядке


class UTM(models.Model):
    address = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'УТМ'
        verbose_name_plural = 'УТМ'

