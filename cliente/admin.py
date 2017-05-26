from django.contrib import admin
from .models import Crianca, Responsavel


class AdminCrianca(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'escola']


class AdminResponsavel(admin.ModelAdmin):
    list_display = ['nome', 'numeroDDD', 'telefone', 'celular']


admin.site.register(Crianca, AdminCrianca)
admin.site.register(Responsavel, AdminResponsavel)
