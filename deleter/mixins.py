import re
import requests
import xml.etree.ElementTree as eltree

def get_utm_doc_urls(address):

    r = requests.request('GET', address)
    answer = r.text
    regexp = re.compile(r'[\n\r\t]')
    clear_answer = regexp.sub(' ', answer)
    root = eltree.fromstring(clear_answer)
    docurls = [child.text.strip() for child in root if child.tag == 'url' ]

    return docurls


def delete_utm_doc(Model, docurl):    
    obj = Model.objects.filter(url='url')
    obj.delete()
    requests.request('DELETE', docurl)


def load(Model, address):
    doc_urls = get_utm_doc_urls(address)
    for url in doc_urls:
        model = Model()
        model.title = url
        model.url = url
        model.save()

