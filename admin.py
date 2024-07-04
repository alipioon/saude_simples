from django.contrib import admin
from .models import tipo_norma, normas
    # , normas, pais, estados, municipios, tipo_norma,\
    # normas, bairros, tp_logradouro, logradouro

def dt_publ(obj):
    return ("%s " % (obj.dt_publicacao.strftime('%d/%m/%Y'))).upper()
dt_publ.short_description = 'Data Publicação'

def dt_assin(obj):
    return ("%s " % (obj.dt_assinatura.strftime('%d/%m/%Y'))).upper()
dt_assin.short_description = 'Data Assinatura'

@admin.register(tipo_norma)
class tipo_normaAdmin(admin.ModelAdmin):
    list_display = ('nom_tipo_norma', 'cod_tipo_norma', 'id')
    search_fields = ['nom_tipo_norma']
    list_per_page = 10

@admin.register(normas)
class normasAdmin(admin.ModelAdmin):
    list_display = ('nom_norma', 'cod_tipo_norma', 'exercicio', dt_publ, dt_assin, 'cod_norma', 'id')
    search_fields = ['nom_norma']
    list_filter = ['exercicio']
    # save_on_top = True
    list_per_page = 10
    admin.site.disable_action('delete_selected')


# def get_pais(obj):
#     return obj.nom_pais.upper()
# get_pais.short_description = 'PAIS'
#
# def get_nacionalidade(obj):
#     return obj.nacionalidade.upper()
# get_nacionalidade.short_description = 'NACIONALIDADE'
#
# def get_sigla(obj):
#     return obj.sigla_3.upper()
# get_sigla.short_description = 'SIGLA'
#
# @admin.register(pais)
# class paisAdmin(admin.ModelAdmin):
#     # list_display = ('cod_pais', 'cod_rais', 'nom_pais', 'nacionalidade', 'sigla_3')
#     # list_display = ('nom_pais', 'nacionalidade', 'sigla_3')
#     list_display = (get_pais, get_nacionalidade, get_sigla, 'cod_pais', 'id')
#     list_per_page = 15
#
# def cod_pais(obj):
#     return str(obj.cod_pais).upper()
# cod_pais.short_description = 'PAIS'
#
# def nom_uf(obj):
#     return str(obj.nom_uf).upper()
# nom_uf.short_description = 'ESTADO'
#
# @admin.register(estados)
# class estadosAdmin(admin.ModelAdmin):
#     list_display = (nom_uf, 'sigla_uf', 'cod_uf', 'id')
#     list_per_page = 15
#
# def estado(obj):
#     return str(obj.cod_uf).upper() #+ estado(filter(cod_uf=obj.cod_uf))
# estado.short_description = 'Estado'
#
# def cidade(obj):
#     return obj.nom_municipio.upper()
# cidade.short_description = 'Cidade'
#
# @admin.register(municipios)
# class municipiosAdmin(admin.ModelAdmin):
#     list_display = (estado, cidade, 'cod_ibge', 'cod_municipio', 'id')
#     # list_display = ('get_parents', cidade, 'cod_ibge', 'cod_municipio', 'id')
#     list_filter = ['cod_uf']
#     search_fields = ['nom_municipio']
#     list_per_page = 20
#
#     # def get_products(self, obj):
#     #     return "\n".join([p.municipios for p in obj.cod_municipio.all()])
#
#     # def get_parents(self):
#     #     return ",".join([str(codigo) for municipios in self.municipios.all()])
#

# def cid_bair(obj):
#     return str(obj.cod_municipio).upper()
# cid_bair.short_description = 'Cidade'

# @admin.register(bairros)
# class bairrosAdmin(admin.ModelAdmin):
#     list_display = ('cod_uf', 'cod_municipio', 'nom_bairro', 'cod_bairro', 'id')
#     list_filter = ['cod_uf']
#     search_fields = ('nom_bairro',)
#     list_per_page = 20
#
# @admin.register(tp_logradouro)
# class tp_logradouroAdmin(admin.ModelAdmin):
#     list_display = ('nom_tipo', 'abreviatura', 'cod_tipo', 'id')
#     list_per_page = 10
#
# def dt_criacao(obj):
#     return ("%s " % (obj.dt_criacao.strftime('%d/%m/%Y'))).upper()
# dt_criacao.short_description = 'Data Criação'
#
# def cod_tipo(obj):
#     return ("%s " % (obj.cod_tipo)).upper()
#
# def nom_logr(obj):
#     return ("%s " % (obj.nom_logradouro)).upper()
#
#
# @admin.register(logradouro)
# class logradouroAdmin(admin.ModelAdmin):
#     # list_display = ('nom_logradouro','cod_tipo', 'cod_uf', 'cod_municipio', dt_criacao, 'cod_norma', 'cod_logradouro', 'id',)
#     list_display = ('nom_logradouro', 'cod_tipo', 'cod_bairro',  dt_criacao, 'cod_norma', 'cod_logradouro')
#     search_fields = ['nom_logradouro']
#     list_per_page = 20
#
# # class Villain(Entity):
# #     ...
# #     is_unique = models.BooleanField(default=True)
# #
# # @admin.register(Villain)
# # class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
# #     ...
# #     change_form_template = "entities/villain_changeform.html"
# #
# #
# #     def response_change(self, request, obj):
# #         if "_make-unique" in request.POST:
# #             matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
# #             matching_names_except_this.delete()
# #             obj.is_unique = True
# #             obj.save()
# #             self.message_user(request, "This villain is now unique")
# #             return HttpResponseRedirect(".")
# #         return super().response_change(request, obj)