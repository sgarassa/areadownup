# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arearis', '0002_auto_20170524_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='tipofile',
            field=models.ForeignKey(verbose_name='Tipo file', to='arearis.FamigliaFile'),
        ),
        migrations.AlterField(
            model_name='news',
            name='azienda',
            field=models.ManyToManyField(verbose_name='Azienda', to='arearis.Azienda'),
        ),
    ]
