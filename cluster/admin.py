from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_url', 'active')

admin.site.register(Service, ServiceAdmin)
    
