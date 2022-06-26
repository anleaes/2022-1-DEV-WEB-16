from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        exclude = ('created_on' , 'updated_on',)