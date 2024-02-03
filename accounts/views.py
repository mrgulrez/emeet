from django.shortcuts import render,  redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.contrib import messages



from .forms import RegisterForm


# Create your views here.
class UserSignupView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



