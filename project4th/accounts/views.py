from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import CustomUserRegistrationForm
# Create your views here.

class UserRegister(CreateView):
    template_name="registration/register.html"
    success_url= reverse_lazy('login')
    form_class = CustomUserRegistrationForm
