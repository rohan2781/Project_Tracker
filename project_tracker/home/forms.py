from django.core import validators
from django import forms
from .models import Client


class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name','second_name','email','password')
        widgets = {
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'second_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
