# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorista', '0005_motorista_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='deficiente',
            field=models.BooleanField(default=False, verbose_name='Aceita Deficiência'),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='capacidadeDeficiente',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
