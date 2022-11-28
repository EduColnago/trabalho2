from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cars

class CarsModel2Form(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ["modelo", "marca", "valor", "observacoes", "fotos"]

class UserModel2Form(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']