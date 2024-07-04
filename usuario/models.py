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

class usuario(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='id', editable=False)
    #nome = models.CharField(max_length=40, verbose_name='CNS', **bnull)
    email = models.CharField(max_length=40, verbose_name='EMAIL', **bnull)
    login = models.CharField(max_length=40, verbose_name='LOGIN', **bnull)

    class Meta:
        db_table = 'public"."usuarios_homolog'  # 'schema"."objeto'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ["id"]
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
       return str(str(self.id) + '  -  ' + str(self.login))

