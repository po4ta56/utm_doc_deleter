import re
import requests
import xml.etree.ElementTree as eltree
from .models import *

def get_utm_doc_urls(address):

    r = requests.request('GET', address)
    answer = r.text
    regexp = re.compile(r'[\n\r\t]')
    clear_answer = regexp.sub(' ', answer)
    root = eltree.fromstring(clear_answer)
    docurls = [child.text.strip() for child in root if child.tag == 'url' ]

    return docurls


def delete_utm_doc(Model, docid):    
    queryset = Model.objects.filter(pk=docid)
    if len(queryset):
        obj = queryset[0]
        docurl = obj.url
        obj.delete()
        requests.request('DELETE', docurl)


def load(Model, address):
    doc_urls = get_utm_doc_urls(address)
    for url in doc_urls:
        model = Model()
        model.title = url
        model.url = url
        model.save()


def load_inbox():
    load(DocumentInboxing, get_address_inbox())


def load_outbox():
    load(DocumentOutboxing, get_address_outbox())




def get_address():
    servers = UTM.objects.all()
    assert len(servers),  ' Адрес UTM не задан!'
    
    return 'http://' + servers[0].address


def get_address_inbox():
    return get_address() + ':8080/opt/out'


def get_address_outbox(): 
    return get_address() + ':8080/opt/in'


def get_utmdoc_text(doc_url):
    