from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        exclude = ('created_on' , 'updated_on',)