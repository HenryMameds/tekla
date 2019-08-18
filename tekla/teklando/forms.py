# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Voluntario


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Voluntario
        fields = (
                    'username',
                    'email',
                    'telefone',
                    'celular',
                    'genero',
                    'data_nascimento',
                    'endereco',
                    'numero',
                    'complemento',
                    'cep',
                    'bairro',
                    'cidade',
                    'estado',
                    'disponibilidade',
                    'escolaridade',
                    'objetivo'
                 )
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Voluntario
        fields = UserChangeForm.Meta.fields
