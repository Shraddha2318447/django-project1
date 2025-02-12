from django.shortcuts import render, redirect  # add redirect, sending to page
from django.urls import reverse_lazy

from django.views.generic import CreateView

# importing django.contrib.auth's user craetion form
from django.contrib.auth


# Create your views here.
class UserRegister(CreateView):

    template_name = 'register.html'
    success_url = reverse_lazy('signin')