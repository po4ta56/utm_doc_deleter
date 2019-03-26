from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views.generic import View

from django.views.generic import DetailView, ListView
from .models import Document

#class IncomingDocView(DetailView):
#    model = IncomingDoc
#    template_name = 'incomindDoc.html'
#    context_object_name = doc
#
#    def get(self):
#        return HttpResponse('detail')



class OutboxingView(View):
    def get(self):
        docid = None
        return HttpResponse(f'здесь будут исходящие документы, docid = {docid}')



def show_inboxing_docs(request, docid=None):
    return HttpResponse(f'здесь будут входящие документы, docid = {docid}')

