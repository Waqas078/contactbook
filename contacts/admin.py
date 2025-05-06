from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone', 'email')
    list_filter = ('user',)
    search_fields = ('name', 'email')
