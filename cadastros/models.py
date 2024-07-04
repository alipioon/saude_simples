from django.db import models
from django.urls import reverse
import calendar
from pytz import timezone
from datetime import datetime
# from django.utils.six import with_metaclass
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField
from django.core.exceptions import ValidationError
# from .fields import LowerCharField
from dateutil.relativedelta import relativedelta
from django.db.models import Count

bnull = dict(blank=True, null=True)
dt_hr = datetime.now()
dt_fim = dt_hr + relativedelta(years=20)
dt_hora = dt_hr.strftime('%d/%m/%Y %H:%M')
exerc_atual = dt_hr.strftime("%Y")


#class tipo_norma(models.Model):
#    cod_tipo_norma = models.AutoField(primary_key=True)
#    nom_tipo_norma = models.CharField(max_length=40, verbose_name='Tipo Norma')
#    cod_cadastro = models.IntegerField(verbose_name='Codigo Cadastro', default=1, editable=False)
#    cod_modulo = models.IntegerField(verbose_name='Codigo Modulo', default=15, editable=False)
#    id = models.IntegerField(verbose_name='id', **bnull, editable=False)

#    class Meta:
#        db_table = 'cadastros"."tipo_norma'  # 'schema"."objeto'
#        verbose_name = '002.Tipo Norma'
#        verbose_name_plural = '002. Tipo Normas'
#        ordering = ["cod_tipo_norma"].reverse()
        # widgets = {'cod_periodicidade': models.IntegerField(attrs={'size': 10})}

#    def clean(self):
#        if tipo_norma.objects.filter(nom_tipo_norma=self.nom_tipo_norma.upper()):
#            raise ValidationError("Já Cadastrado: " + self.nom_tipo_norma.upper())

#    def save(self, force_insert=False, force_update=False, *args, **kwargs):
#        self.nom_tipo_norma = self.nom_tipo_norma.upper()
#        if not self.id:
#            self.cod_tipo_norma = tipo_norma.objects.all().last().cod_tipo_norma + 1 \
#                if tipo_norma.objects.all().last() \
#                else 1
#        self.id = self.cod_tipo_norma
#        super().save(*args, **kwargs)

#    def __str__(self):
#       # return str(self.cod_tipo_norma) + '  -  ' + str(self.nom_tipo_norma)
#       return str(self.nom_tipo_norma)


#class normas(models.Model):
#    cod_norma = models.AutoField(primary_key=True)
#    cod_tipo_norma = models.ForeignKey(tipo_norma, db_column='cod_tipo_norma', on_delete=models.PROTECT)
#    exercicio = models.CharField(max_length=4, verbose_name='Exercicio', default=exerc_atual)
#    nom_norma = models.CharField(max_length=80, verbose_name='Nome Norma')
#    descricao = models.TextField(**bnull)
#    num_norma = models.CharField(max_length=30, verbose_name='Numero Norma')
#    dt_publicacao = models.DateField(null=True, verbose_name='Data Publicação', default=dt_hr)
#    dt_assinatura = models.DateField(null=True, verbose_name='Data Assinatura', default=dt_hr)
#    id = models.IntegerField(verbose_name='id', **bnull, editable=False)

#    class Meta:
#        db_table = 'cadastros"."norma'  # 'schema"."objeto'
#        verbose_name = '003.Normas'
#        verbose_name_plural = '003.Normas'
#        ordering = ["cod_norma"].reverse()
#        # widgets = {'cod_periodicidade': models.IntegerField(attrs={'size': 10})}

#    def clean(self):
#        if normas.objects.filter(nom_norma=self.nom_norma.upper()). \
#                filter(cod_tipo_norma=self.cod_tipo_norma).filter(descricao=self.descricao). \
#                filter(exercicio=self.exercicio).filter(num_norma=self.num_norma). \
#                filter(dt_publicacao=self.dt_publicacao).filter(dt_assinatura=self.dt_assinatura):
#            raise ValidationError("Já Cadastrado: " + str(self.cod_tipo_norma) + "  -  " + \
#                                  self.exercicio + '  -  ' + self.nom_norma.upper())

#    def save(self, force_insert=False, force_update=False, *args, **kwargs):
#        self.nom_norma = self.nom_norma.upper()
#        if not self.id:
#            self.cod_norma = normas.objects.all().last().cod_norma + 1 \
#                if normas.objects.all().last() \
#                else 1
#        self.id = self.cod_norma
#        super().save(*args, **kwargs)
#
#    def __str__(self):
#       return str(self.nom_norma)


# class pais(models.Model):
#     cod_pais = models.IntegerField(verbose_name='Codigo Pais', null=True, blank=True, editable=False)
#     nom_pais = models.CharField(max_length=20, verbose_name='Nome')
#     sigla_3 = models.CharField(max_length=3, verbose_name='Sigla', **bnull)
#     nacionalidade = models.CharField(max_length=80, verbose_name='Nacionalidade', **bnull)
#     cod_rais = models.IntegerField(verbose_name='Codigo Rais', **bnull, editable=False)
#
#     class Meta:
#         db_table = 'cadastros"."sw_pais'  # 'schema"."objeto'
#         verbose_name = '005.Paises'
#         verbose_name_plural = '005.Paises'
#         ordering = ["cod_pais"].reverse()
#
#     def __str__(self):
#        return str(self.nom_pais)
#
#     def clean(self):
#         if self.sigla_3 in [None, '']:
#             self.sigla_3 = "NI"
#
#         if pais.objects.filter(nom_pais=self.nom_pais.upper()).\
#                 filter(sigla_3=self.sigla_3.upper()).\
#                 filter(nacionalidade=self.nacionalidade.upper()):
#             raise ValidationError("Já Cadastrado: " + self.nom_pais.upper())
#
#     def save(self, *args, **kwargs):
#         if self.sigla_3 in [None, '']:
#             self.sigla_3 = "NI"
#         if self.nacionalidade in [None, '']:
#             self.nacionalidade="Não Informada"
#
#         self.sigla_3 = self.sigla_3.upper()
#         self.nom_pais = self.nom_pais.upper()
#         self.nacionalidade = self.nacionalidade.upper()
#
#         if not self.id:
#             self.cod_pais = pais.objects.all().last().cod_pais + 1 \
#                 if pais.objects.all().last() \
#                 else 1
#         self.id = self.cod_pais
#
#         if not self.cod_rais:
#             self.cod_rais = self.cod_pais
#         super().save(*args, **kwargs)
#
#     # def delete(self, *args, **kwargs):
#     #     for paises in pais.objects.filter(id__gt=self.id):
#     #         paises.cod_pais = paises.cod_pais - 1
#     #         paises.save()
#     #     paises.objects.filter(id=self.id).delete()
#
#
# class estados(models.Model):
#     cod_uf = models.IntegerField(null=True, blank=True, editable=False)
#     cod_pais = models.ForeignKey(pais, db_column='cod_pais', related_name='Pais', on_delete=models.PROTECT, verbose_name='Pais' , default=1)
#     nom_uf = models.CharField(max_length=50, verbose_name='Estado')
#     sigla_uf = models.CharField(max_length=2, verbose_name='Sigla')
#
#     class Meta:
#         db_table = 'cadastros"."sw_uf'  # 'schema"."objeto'
#         verbose_name = '006.Estados'
#         verbose_name_plural = '006.Estados'
#         ordering = ["cod_uf"].reverse()
#         # ordering = ["sigla_uf"]
#         # widgets = {'cod_paisperiodicidade': models.IntegerField(attrs={'size': 10})}
#
#     def __str__(self):
#        # return str(self.nom_uf + " - " + self.sigla_uf)
#        return str(self.nom_uf)
#
#     # def clean(self):
#     #     if estados.objects.filter(nom_uf=self.nom_uf):
#     #         raise ValidationError("Já Cadastrado: " + self.nom_uf)
#
#     def clean(self):
#         if estados.objects.filter(nom_uf=self.nom_uf.upper()):
#             raise ValidationError("Já Cadastrado: " + self.nom_uf.upper())
#
#     def save(self, force_insert=False, force_update=False, *args, **kwargs):
#         self.sigla_uf = self.sigla_uf.upper()
#         self.nom_uf = self.nom_uf.upper()
#
#         if not self.id:
#             self.cod_uf = estados.objects.all().last().cod_uf + 1 \
#                 if estados.objects.all().last() \
#                 else 1
#             self.id = self.cod_uf
#         super().save(*args, **kwargs)
#
#     # def delete(self, *args, **kwargs):
#     #     for uf in estado.objects.filter(id__gt=self.id):
#     #         uf.cod_pais = uf.cod_pais - 1
#     #         uf.save()
#     #     estado.objects.filter(id=self.id).delete()
#
#
# class municipios(models.Model):
#     cod_municipio = models.IntegerField(null=True, blank=True, editable=False)
#     # cod_municipio = (estados.objects.values('cod_municipio').annotate(dcount=Count('cod_municipio')).order_by())
#     cod_uf = models.ForeignKey(estados, db_column='cod_uf', related_name='UF', on_delete=models.PROTECT, verbose_name='Estado')
#     nom_municipio = models.CharField(max_length=35, verbose_name='Nome Cidade')
#     cod_ibge = models.CharField(max_length=5, **bnull, verbose_name='Codigo Ibge')
#
#     class Meta:
#         db_table = 'cadastros"."sw_municipio'  # 'schema"."objeto'
#         verbose_name = '007.Cidade'
#         verbose_name_plural = '007.Cidades'
#         ordering = ["id"]
#         # ordering = ["nom_municipio"]
#
#     # def get_products(self, obj):
#     #     return "\n".join([p.municipios for p in obj.cod_municipio.all()])
#
#     def __str__(self):
#        return str(self.nom_municipio)
#
#     def clean(self):
#         if municipios.objects.filter(nom_municipio=self.nom_municipio.upper()). \
#            filter(cod_uf=self.cod_uf):
#             raise ValidationError("Já Cadastrado: " + str(self.cod_uf) + "  -  " + self.nom_municipio.upper())
#
#     def save(self, force_insert=False, force_update=False, *args, **kwargs):
#         self.nom_municipio = self.nom_municipio.upper()
#         # raise ValidationError("id: " + str(id))
#
#         if not self.id:
#             self.cod_municipio = municipios.objects.all().last().id + 1\
#                 if municipios.objects.all().last() \
#                 else 1
#         # raise ValidationError("cod_municipio: " + str(xx))
#             self.id = self.cod_municipio
#         super().save(*args, **kwargs)
#
#     # def delete(self, *args, **kwargs):
#     #     for municipio in municipios.objects.filter(id__gt=self.id):
#     #         municipios.cod_municipio = municipio.cod_municipio - 1
#     #         municipios.save()
#     #     municipios.objects.filter(id=self.id).delete()
#
#
# class bairros(models.Model):
#     cod_bairro = models.IntegerField(null=True, blank=True, editable=False)
#     cod_uf = models.ForeignKey(estados, db_column='cod_uf', on_delete=models.PROTECT, verbose_name='Estado')
#     cod_municipio =ChainedForeignKey(municipios, db_column='cod_municipio',
#         chained_field="cod_uf",
#         chained_model_field="cod_uf",
#         show_all=False,
#         auto_choose=True,
#         sort=True, verbose_name='Cidade')
#     nom_bairro = models.CharField(max_length=30, verbose_name='Bairro')
#
#     class Meta:
#         db_table = 'cadastros"."sw_bairro'  # 'schema"."objeto'
#         verbose_name = '008.Bairros'
#         verbose_name_plural = '008.Bairros'
#         ordering = ["cod_bairro"]
#         # ordering = ["cod_municipio"]
#
#     def __str__(self):
#        return str(self.nom_bairro)
#
#     def clean(self):
#         if bairros.objects.filter(nom_bairro=self.nom_bairro.upper()). \
#            filter(cod_uf=self.cod_uf).filter(cod_municipio=self.cod_municipio):
#             raise ValidationError("Já Cadastrado: " + str(self.cod_uf) + '  -  ' + str(self.cod_municipio) +
#                                   '  -  ' + self.nom_bairro.upper())
#
#     def save(self, force_insert=False, force_update=False, *args, **kwargs):
#         self.nom_bairro = self.nom_bairro.upper()
#
#         if not self.id:
#             self.cod_bairro = bairros.objects.all().last().id + 1 \
#                 if bairros.objects.all().last() \
#                 else 1
#             self.id = self.cod_bairro
#         super().save(*args, **kwargs)
#
#     # def delete(self, *args, **kwargs):
#     #     for bairro in sw_bairro.objects.filter(id__gt=self.id):
#     #         bairro.cod_bairro = bairro.cod_bairro - 1
#     #         bairro.save()
#     #     sw_bairro.objects.filter(id=self.id).delete()
#
#
# # class TipoLogr(models.CharField):
# #     def __init__(self, *args, **kwargs):
# #         super(TipoLogr, self).__init__(*args, **kwargs)
# #
# #     def get_prep_value(self, value):
# #         return str(value).upper()
#
# class tp_logradouro(models.Model):
#     cod_tipo = models.IntegerField(verbose_name= 'Codigo', **bnull)
#     nom_tipo = models.CharField(max_length=15, verbose_name='Tipo de Logradouro: ')
#     abreviatura = models.CharField(max_length=5, **bnull, verbose_name='Abreviatura: ')
#
#     class Meta:
#         db_table = 'cadastros"."sw_tp_logradouro'  # 'schema"."objeto'
#         verbose_name = '014. Tipos de Logradouros'
#         verbose_name_plural = '014. Tipos de Logradouros'
#         ordering = ["id" , "nom_tipo"]
#
#     def __str__(self):
#        return str(self.nom_tipo)
#
#     # OK FUNCIONOU
#     # def clean(self):
#     #     if self.nom_tipo.upper() == 'KK':
#     #         raise ValidationError("Errado não é KK")
#
#     def clean(self):
#         if tp_logradouro.objects.filter(nom_tipo=self.nom_tipo.upper()):
#             raise ValidationError("Já Cadastrado: " + self.nom_tipo.upper())
#
#     def save(self, force_insert=False, force_update=False, *args, **kwargs):
#         self.nom_tipo = self.nom_tipo.upper()
#         if not self.id:
#             self.cod_tipo = tp_logradouro.objects.all().last().id + 1 \
#                 if tp_logradouro.objects.last() \
#                 else 1
#             self.id = self.cod_tipo
#         # raise ValidationError("codigo tipo: " + str(self.cod_tipo))
#
#         super().save(*args, **kwargs)
#
# class logradouro(models.Model):
#     cod_municipio = models.ForeignKey(municipios, db_column='cod_municipio', on_delete=models.PROTECT, verbose_name='Cidade', default=1)
#     cod_bairro =ChainedForeignKey(bairros, db_column='cod_bairro',
#          chained_field="cod_municipio",
#          chained_model_field="cod_municipio",
#          show_all=False,
#          auto_choose=True,
#          sort=True, verbose_name='bairro')
#     cod_logradouro = models.IntegerField(verbose_name='Codigo', **bnull, editable=False)
#     cod_tipo = models.ForeignKey(tp_logradouro, db_column='cod_tipo', on_delete=models.PROTECT, verbose_name='Tipo')
#     nom_logradouro = models.CharField(max_length=60, verbose_name='Logradouro')
#     cod_norma = models.ForeignKey(normas, db_column='cod_norma', on_delete=models.CASCADE, verbose_name='Norma', default=1)
#     dt_criacao = models.DateField(null=True, verbose_name='Data Criacao', default=dt_hr)
#
#     class Meta:
#         db_table = 'cadastros"."sw_logradouro'  # 'schema"."objeto'
#         verbose_name = '015. Logradouro'
#         verbose_name_plural = '015. Logradouros'
#         ordering = ["cod_logradouro"]
#
#     def __str__(self):
#        return str(self.nom_logradouro)
#
#     def clean(self):
#         if logradouro.objects.filter(nom_logradouro=self.nom_logradouro.upper()). \
#                 filter(cod_tipo=self.cod_tipo).filter(cod_bairro=self.cod_bairro):
#             raise ValidationError("Já Cadastrado: " + str(self.cod_tipo) + ' ' + self.nom_logradouro.upper() +
#                                   ' em ' + str(self.cod_bairro))
#
#     def save(self, force_insert=False, force_update=False, *args, **kwargs):
#         self.nom_logradouro = self.nom_logradouro.upper()
#         if not self.id:
#             self.cod_logradouro = logradouro.objects.all().last().cod_logradouro + 1 \
#                 if logradouro.objects.all().last() \
#                 else 1
#         self.id = self.cod_logradouro
#         # raise ValidationError("cod logradouro: " + str(self.cod_logradouro))
#         super().save(*args, **kwargs)
