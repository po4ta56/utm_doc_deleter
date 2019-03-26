from django.contrib import admin

from .models import DocumentInboxing, DocumentOutboxing

@admin.register(DocumentInboxing, DocumentOutboxing)
class AuthorAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Document, AuthorAdmin)
