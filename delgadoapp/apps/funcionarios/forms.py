from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        exclude = ('created_on' , 'updated_on',)