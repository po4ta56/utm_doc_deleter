from django.contrib import admin
from django.urls import path

from .views import OutboxingView, SettingsView, show_inboxing_docs, redirect_to_start


urlpatterns = [
    path('', redirect_to_start),
    path('inbox/<int:docid>', show_inboxing_docs),
    path('inbox/', show_inboxing_docs, name='inbox'),  
    path('outbox/<int:docid>', show_inboxing_docs),
    path('outbox/', OutboxingView.as_view(), name='outbox'),  
    path('setting/', SettingsView.as_view(), name='setting'),  
]