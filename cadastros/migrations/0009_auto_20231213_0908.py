# Generated by Django 3.2.22 on 2023-12-13 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_auto_20231213_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normas',
            name='dt_assinatura',
            field=models.DateField(default=datetime.datetime(2023, 12, 13, 9, 8, 6, 556617), null=True, verbose_name='Data Assinatura'),
        ),
        migrations.AlterField(
            model_name='normas',
            name='dt_publicacao',
            field=models.DateField(default=datetime.datetime(2023, 12, 13, 9, 8, 6, 556617), null=True, verbose_name='Data Publicação'),
        ),
    ]
