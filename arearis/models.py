from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from django.conf import settings


class Azienda(models.Model):
    AZIENDA = 'AZ'
    STUDIO = 'ST'
    TIPO = (
    (AZIENDA, 'AZIENDA'),
    (STUDIO, 'STUDIO'),
    )
    ragsoc = models.CharField(max_length=50, verbose_name='Ragione Sociale')
    piva = models.CharField(max_length=20, verbose_name='Partita IVA')
    codfisc = models.CharField(max_length=20, verbose_name='Codice Fiscale')
    indirizzo = models.CharField(max_length=70, verbose_name='Indirizzo')
    localita = models.CharField(max_length=50, verbose_name='Città')
    prov = models.CharField(max_length=2, verbose_name='Pr')
    cap = models.CharField(max_length=5, verbose_name='CAP')
    tipologia = models.CharField(
		max_length=2, 
		choices = TIPO, 
		default = AZIENDA,
	verbose_name='Tipologia')
    flagAzienda = models.BooleanField(verbose_name= 'Azienda di riferimento')
    email = models.EmailField(max_length=50, blank = False, verbose_name='E-mail')
    utente = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Utente')
    def __str__(self):
	     return '%s %s ' % (self.ragsoc, self.piva)
    class Meta:
	    verbose_name_plural = 'Aziende'

	

class FamigliaFile(models.Model):
    descrizione = models.CharField(max_length=20)
    def __str__(self):
	    return '%s ' % self.descrizione
    class Meta:
	    verbose_name_plural = 'Tipo File'


class File(models.Model):
    utente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
    azienda = models.ForeignKey(Azienda, verbose_name='Azienda')
    titolo = models.CharField(max_length=15)
    upload = models.FileField(upload_to = 'upload/')
    tipofile = models.ForeignKey(FamigliaFile, verbose_name='Tipo file')
    created_date = models.DateTimeField(
            default=timezone.now)
    flag_vis = models.BooleanField(verbose_name= 'File visualizzato', blank=True)
    def __str__(self):
	    return u"%s %s" % (self.titolo, self.upload)
    class Meta:
	    verbose_name_plural = 'File'



class News(models.Model):
    utente = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Utente')
    azienda = models.ManyToManyField(Azienda, verbose_name='Azienda')
    titolo = models.CharField(max_length=10)
    descrizione = models.CharField(max_length=100)    
    flag_vis = models.BooleanField(verbose_name= 'News visualizzata')
    created_date = models.DateTimeField(
            default=timezone.now)
    def __str__(self):
	    return u"%s %s" % (self.titolo, self.descrizione)
    class Meta:
	    verbose_name_plural = 'News'
