from django import forms
from .models import Genero

class GeneroForm(forms.ModelForm):

    class Meta:
        model = Genero
        exclude = ('created_on' , 'updated_on',)