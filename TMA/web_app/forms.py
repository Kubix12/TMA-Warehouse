from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Request


# -- Register/Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# -- Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['employee_name', 'item', 'unit_of_measurement', 'quantity', 'price_without_vat', 'comment']
