from django.contrib import admin
from .models import Escola


class EscolaAdmin(admin.ModelAdmin):
    list_display = ['nomeEscola', 'endereco']

admin.site.register(Escola, EscolaAdmin)