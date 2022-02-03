from django.core import validators
from django import forms
from .models import Client

'''class clients(forms.ModelForm):
    class Meta:
        model=user
        fields = ('first_name','last_name','email','password','id')
        widgets = {
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }'''

class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name','last_name','email','password')
        widgets = {
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
