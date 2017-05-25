# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arearis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='azienda',
            field=models.ManyToManyField(to='arearis.Azienda', verbose_name='Azienda'),
        ),
    ]
