from django.contrib import admin
from .models import municipe
    # , normas, pais, estados, municipios, tipo_norma,\
    # normas, bairros, tp_logradouro, logradouro

def dt_nasc(obj):
    return ("%s " % (obj.data_nascimento.strftime('%d/%m/%Y'))).upper()
dt_nasc.short_description = 'Data Nascimento'

def dt_assin(obj):
    return ("%s " % (obj.dt_assinatura.strftime('%d/%m/%Y'))).upper()
dt_assin.short_description = 'Data Assinatura'

@admin.register(municipe)
class municipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo_cns', 'cpf_numero', dt_nasc, 'nome_mae', 'nome_pai')
    search_fields = ['nome','codigo_cns','cpf_numero','nome_mae','nome_pai']
    list_per_page = 20
