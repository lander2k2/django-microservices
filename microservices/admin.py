from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from .models import Service


class MicroservicesAdminSite(admin.AdminSite):
    site_header = 'Microservices Administration'
    site_title = 'Microservices Admin'
    index_title = 'MicroServices Admin'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')


services_admin_site = MicroservicesAdminSite(name='microservices_admin')
services_admin_site.register(User, UserAdmin)
services_admin_site.register(Group, GroupAdmin)
services_admin_site.register(Service, ServiceAdmin)

