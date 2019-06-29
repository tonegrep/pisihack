from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import PisiUserCreationForm


class SignUpView(CreateView):
    form_class = PisiUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
