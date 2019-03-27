from django.db import models


class DocumentInboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящие документы'

    
class DocumentOutboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'
        ordering = ('-title',) # сортировка по умолчанию в обратном порядке