# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arearis', '0003_auto_20170524_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='azienda',
        ),
        migrations.AddField(
            model_name='file',
            name='azienda',
            field=models.ForeignKey(default=2, verbose_name='Azienda', to='arearis.Azienda'),
            preserve_default=False,
        ),
    ]
