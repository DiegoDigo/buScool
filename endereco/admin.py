from django.contrib import admin
from .models import Logradouro, Cidade


class LogradouroAdmin(admin.ModelAdmin):
    list_display = ['logradouro', 'numero', 'cidade']


class CidadeAdmin(admin.ModelAdmin):
    list_display = ['cidade', 'uf']

admin.site.register(Logradouro, LogradouroAdmin)
admin.site.register(Cidade, CidadeAdmin)
