from django.core import validators
from django import forms
from .models import Client
from manager.models import Developer

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
class DevRegistration(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ('first_name','last_name','email','password')
        widgets = {
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }


class ClientRegistration(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('username','last_name','email','password')
        widgets = {
        'username' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
