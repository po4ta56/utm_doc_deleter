from django.contrib import admin
from django.urls import path

from .views import OutboxingView, SettingsView, show_inboxing_docs, redirect_to_start, \
    clear_all, reload_docs, InboxingDocsView, OutboxingDocsView, remove_outbox_doc, remove_inbox_doc, \
    remove_all_inbox_doc, remove_all_outbox_doc


urlpatterns = [
    path('', redirect_to_start),
    
    path('inbox/', InboxingDocsView.as_view(), name='inbox'),  
    path('inbox/<int:docid>', show_inboxing_docs),
    path('inbox/remove/<int:docid>', remove_inbox_doc),
    path('inbox/removeall', remove_all_inbox_doc, name='removeall'),
    
    path('outbox/', OutboxingDocsView.as_view(), name='outbox'),  
    path('outbox/<int:docid>', show_inboxing_docs),
    path('outbox/remove/<int:docid>', remove_outbox_doc),
    path('inbox/removeall', remove_all_outbox_doc, name='removeall'),
        
    path('setting/', SettingsView.as_view(), name='setting'),
    path('setting/clearall', clear_all, name='clear_docs'),
    path('setting/reload', reload_docs, name='reload_docs'),  
]