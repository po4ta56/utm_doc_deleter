from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from django.views.generic import View

from django.views.generic import DetailView, ListView
from .models import DocumentInboxing, DocumentOutboxing

#class IncomingDocView(DetailView):
#    model = IncomingDoc
#    template_name = 'incomindDoc.html'
#    context_object_name = doc
#
#    def get(self):
#        return HttpResponse('detail')

class OutboxingDocsView(ListView):
    template_name = 'deleter/docs_list.html'
    model = DocumentOutboxing

    def dispatch(self, request, *args, **kwargs):
        self.sort_field = request.GET.get('sort_field')
        return super(OutboxingDocsView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = DocumentOutboxing.objects.all()
        if self.sort_field:
            queryset.order_by(self.sort_field)[:10]
        return queryset


class OutboxingView(View):
    def get(self, request):
        #docid = None
        #return HttpResponse(f'здесь будут исходящие документы, docid = {docid}')
        return render(request, 'base.html')



def show_inboxing_docs(request, docid=None):
    #return HttpResponse(f'здесь будут входящие документы, docid = {docid}')
    return render(request, 'base.html')


def redirect_to_start(request):
    return redirect('inbox')
    