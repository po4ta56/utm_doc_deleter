from django.contrib import admin
from django.urls import path

from .views import OutboxingView, SettingsView, show_inboxing_docs, redirect_to_start, clear_all, reload_docs


urlpatterns = [
    path('', redirect_to_start),
    path('inbox/<int:docid>', show_inboxing_docs),
    path('inbox/', show_inboxing_docs, name='inbox'),  
    path('outbox/<int:docid>', show_inboxing_docs),
    path('outbox/', OutboxingView.as_view(), name='outbox'),  
    path('setting/', SettingsView.as_view(), name='setting'),
    path('setting/clearall', clear_all, name='clear_docs'),
    path('setting/reload', reload_docs, name='reload_docs'),  
]