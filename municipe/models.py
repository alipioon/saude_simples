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

class municipe(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', editable=False)
    codigo_cns = models.CharField(max_length=40, verbose_name='CNS', **bnull)
    cpf_numero = models.CharField(max_length=40, verbose_name='CPF', **bnull)
    nome = models.CharField(max_length=80, verbose_name='NOME')
    data_nascimento = models.DateField(null=True, verbose_name='Data Nascimento', default=dt_hr)
    nome_mae = models.CharField(max_length=80, verbose_name='NOME MAE', **bnull)
    nome_pai = models.CharField(max_length=80, verbose_name='NOME PAI', **bnull)

    class Meta:
        db_table = 'public"."municipes_homolog'  # 'schema"."objeto'
        verbose_name = 'Municipe'
        verbose_name_plural = 'Municipes'
        ordering = ["nome"]
        #ordering = ["id"].reverse()
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

    def __str__(self):
       # return str(self.cod_tipo_norma) + '  -  ' + str(self.nom_tipo_norma)
       return str(str(self.id) + '  -  ' + str(self.nome))


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
        # widgets = {'cod_periodicidade': models.IntegerField(attrs={'size': 10})}

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

#    def __str__(self):
#       return str(self.nom_norma)
