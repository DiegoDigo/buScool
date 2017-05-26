from django.contrib import admin
from .models import Veiculo, Motorista


class AdminMotorista(admin.ModelAdmin):
    list_display = ['nome', 'apelido','categoria', 'numeroDDD', 'telefone', 'celular' ,'veiculo']

admin.site.register(Veiculo)
admin.site.register(Motorista, AdminMotorista)