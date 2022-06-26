from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    
    class Meta:
        model = Projeto
        exclude = ('projeto', 'created_on' , 'updated_on')