from django.contrib import admin

from .models import *

@admin.register(DocumentInboxing, DocumentOutboxing, UTM)
class AuthorAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Document, AuthorAdmin)
