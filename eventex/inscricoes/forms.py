from django import forms

class FormInscricoes(forms.Form):
    name = forms.CharField(label='Nome');
    cpf = forms.CharField(label='CPF');
    email = forms.EmailField(label='E-mail');
    phone = forms.CharField(label='Fone');