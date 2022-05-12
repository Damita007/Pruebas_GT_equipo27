from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
#from django.contrib.auth.forms import UserCreationForm
#from rest_framework import generics
#from . import models
#from . import serializers


# class UserListView(generics.CreateAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializers_class = serializers.UserSerializer


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

# from .forms import CustomUserCreationForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"