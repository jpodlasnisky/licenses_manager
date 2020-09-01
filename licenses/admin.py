from django.contrib import admin
from .models import License, Client
# Register your models here.


class ListLicenses(admin.ModelAdmin):
    """ Lista Licenças no Admin """
    list_display = ('client', 'package', 'license_type')


class ListClients(admin.ModelAdmin):
    """ Lista Clientes no Admin """
    list_display = ('client_name',)


admin.site.register(License, ListLicenses)
admin.site.register(Client, ListClients)
