from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from django.views.generic import View

from django.views.generic import DetailView, ListView
from .models import DocumentInboxing, DocumentOutboxing, UTM

class SettingsView(DetailView):
    model = UTM
    template_name = 'settings.html'
    #context_object_name = doc

    #def get(self):
    #    return HttpResponse('detail')

    #def get_queryset(self):
    #    queryset = UTM.objects.all()
    #    if len(queryset) == 0:
    #        utm = UTM()
    #        utm.addres = '127.0.0.1'
    #        utm.save()
    #        queryset = UTM.objects.all()
    #    return queryset[:1]

    def dispatch(self, request, *args, **kwargs):
        print(request.GET)
        return super(SettingsView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        queryset = UTM.objects.all()
        if len(queryset) == 0:
            utm = UTM()
            utm.addres = '127.0.0.1'
            utm.save()
            queryset = UTM.objects.all()
        return queryset[0]
        

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
    return redirect('setting')


def clear_all(request):
    DocumentInboxing.objects.all().delete()
    DocumentOutboxing.objects.all().delete()
    return redirect('setting')


def reload_docs(request):
    DocumentInboxing.Load()
    DocumentOutboxing.Load()
    return redirect('setting')
    