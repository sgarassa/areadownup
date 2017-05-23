from django.contrib import admin
from arearis.models import *
from django import forms



class AziendeOption(admin.ModelAdmin):
	list_display = ('ragsoc', 'piva','codfisc', 'indirizzo', 'localita')
	search_fields = ('ragsoc', 'piva','codfisc',)


class FamigliaFileOption(admin.ModelAdmin):
	list_display = ('descrizione',)
	search_fields = ('descrizione',)


class FileFileOption(admin.ModelAdmin):
	list_display = ('utente', 'titolo', 'upload', 'tipofile', 'created_date', 'flag_vis')
	search_fields = ('utente', 'titolo','created_date',)
	def azie(self, File):
		return File.azienda.ragsoc

class NewsFileOption(admin.ModelAdmin):
	list_display = ('utente', 'titolo', 'descrizione', 'flag_vis', 'created_date')
	search_fields = ('utente', 'titolo', 'descrizione', 'created_date',)
	raw_id_fields = ('azienda',)


admin.site.register(Azienda, AziendeOption)
admin.site.register(FamigliaFile, FamigliaFileOption)
admin.site.register(File, FileFileOption)
admin.site.register(News, NewsFileOption)

