"""
Permite crear/modificar usuarios desde la aplicación de administración 
y también dentro de nuestro propio proyecto.
"""
#from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields                   #("email", "password") 
           