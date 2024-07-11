from typing import Any
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length= 50)
    lastname = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ( 'firstname', 'lastname', 'email', 'password1','password2')

    def save(self, commit = True) -> Any:
        user = super(UserRegisterationForm,self).save(commit= False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["email"]
        user.firstname = self.cleaned_data["firstname"]
        user.lastname = self.cleaned_data["lastname"]

        if commit:
            user.save()
        return user



