import re
from django import forms
from authentication.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm

class UserForm(forms.ModelForm):

    password_confirmation = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'data-validation' : 'strength',
                'data-validation-strength' : '2'
                }
            )
        )
    password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'data-validation' : 'confirmation'
                }
            )
        )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

        widgets = {
            'username': forms.TextInput(attrs = {
                'class' : 'form-control',
                'data-validation' : 'custom',
                'data-validation-regexp' : '^[\w@.+-]+$'
                }),
            'first_name' : forms.TextInput(attrs = {
                'class' : 'form-control'
                }),
            'last_name' : forms.TextInput(attrs = {
                'class' : 'form-control'
                }),
            'email' : forms.TextInput(attrs = {
                'class' : 'form-control', 'data-validation' : 'email'
                }),
        }
