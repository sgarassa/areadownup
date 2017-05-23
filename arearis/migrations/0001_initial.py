# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Azienda',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ragsoc', models.CharField(verbose_name='Ragione Sociale', max_length=50)),
                ('piva', models.CharField(verbose_name='Partita IVA', max_length=20)),
                ('codfisc', models.CharField(verbose_name='Codice Fiscale', max_length=20)),
                ('indirizzo', models.CharField(verbose_name='Indirizzo', max_length=70)),
                ('localita', models.CharField(verbose_name='Città', max_length=50)),
                ('prov', models.CharField(verbose_name='Pr', max_length=2)),
                ('cap', models.CharField(verbose_name='CAP', max_length=5)),
                ('tipologia', models.CharField(default='AZ', choices=[('AZ', 'AZIENDA'), ('ST', 'STUDIO')], verbose_name='Tipologia', max_length=2)),
                ('flagAzienda', models.BooleanField(verbose_name='Azienda di riferimento')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=50)),
                ('utente', models.ManyToManyField(verbose_name='Utente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aziende',
            },
        ),
        migrations.CreateModel(
            name='FamigliaFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('descrizione', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Tipo File',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=15)),
                ('upload', models.FileField(upload_to='upload/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('flag_vis', models.BooleanField(verbose_name='File visualizzato')),
                ('azienda', models.ManyToManyField(to='arearis.Azienda')),
                ('tipofile', models.ForeignKey(to='arearis.FamigliaFile')),
                ('utente', models.ForeignKey(verbose_name='Utente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'File',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=10)),
                ('descrizione', models.CharField(max_length=100)),
                ('flag_vis', models.BooleanField(verbose_name='News visualizzata')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('azienda', models.ManyToManyField(to='arearis.Azienda')),
                ('utente', models.ForeignKey(verbose_name='Utente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
