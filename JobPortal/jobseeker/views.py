from django.shortcuts import render
from jobseeker.models import MyUser,Applicant,Profile
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout

# Create your views here.
