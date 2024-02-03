from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, label="First Name", required=True),
    last_name = forms.CharField(max_length=100, label="Last Name", required=True),
    username = forms.CharField(max_length=100, label="Username", required=True),
    email = forms.EmailField(label="Email", required=True),
    password1 = forms.CharField(label="Password",  required=True),
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput, required=True ),

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']