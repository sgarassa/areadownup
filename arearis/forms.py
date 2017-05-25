from django import forms

from .models import File



class DocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('azienda', 'titolo', 'upload', 'tipofile',  'flag_vis',)

class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('azienda', 'titolo', 'upload', 'tipofile',)

#class FileForm(forms.Form):
#	upload = forms.FileField(
#		label='seleziona un file',
#		help_text='max. 42 megabytes'
#	)
