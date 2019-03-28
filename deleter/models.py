from django.db import models

import requests
from deleter.mixins import load


class DocumentInboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящие документы'

    def Load():
        address = UTM.get_address_inbox()
        load(self, address)
        

    
class DocumentOutboxing(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящие документы'
        ordering = ('-title',) # сортировка по умолчанию в обратном порядке

    def Load(self):
        address = UTM.get_address_outbox()
        load(self, address)



class UTM(models.Model):
    address = models.CharField(max_length=15)

    def get_address(self):
        servers = UTM.objects.all()
        assert len(servers),  ' Адрес UTM не задан!'
        
        return servers[0].address

    def get_address_inbox(self):
        return self.get_address + ':8080/opt/out'

    def get_address_outbox(self): 
        return self.get_address + ':8080/opt/in'
