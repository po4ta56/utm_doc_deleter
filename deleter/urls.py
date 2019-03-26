from django.contrib import admin
from django.urls import path

from .views import OutboxingView, show_inboxing_docs


urlpatterns = [
    path('inbox/<int:docid>', show_inboxing_docs),
    path('inbox/', show_inboxing_docs, name='inbox'),  
    path('outbox/<int:docid>', show_inboxing_docs),
    path('outbox/', OutboxingView.as_view(), name='outbox'),  
]