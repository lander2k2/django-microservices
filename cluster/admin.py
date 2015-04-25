from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active')

admin.site.register(Service, ServiceAdmin)
    
