from django import forms
from . models import Clientes

class FormClientes(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude =()