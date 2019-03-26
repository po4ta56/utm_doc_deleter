from django.contrib import admin

from .models import Document

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, AuthorAdmin)
