from django.forms import ModelForm
from django import forms
from .models import MyUser,Profile,Applicant
from .admin import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model=MyUser
        fields=["username","email","role","password1","password2"]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "role": forms.Select(attrs={'class': 'form-control'})
        }

class UserSigninForm(forms.Form):
    email =forms.CharField(max_length=30, widget=(forms.EmailInput(attrs={'class': 'form-control'})))
    password =forms.CharField(max_length=25, widget=(forms.PasswordInput(attrs={'class': 'form-control'})))

#  -----------------------------------------------------------------------------------------------------------------------------

class ProfileAddForm(ModelForm):
    mobile = forms.CharField(max_length=10, label="Phone", widget=(forms.TextInput(attrs={'class': 'form-control'})))
    address=forms.CharField(max_length=150,widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model=Profile
        fields=["name","email","mobile","dob","gender","address","graduation","post_graduation","experiance","resume"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "dob": forms.DateInput(attrs={'class': 'form-control'}),
            "gender": forms.Select(attrs={'class': 'form-control'}),
            "graduation": forms.TextInput(attrs={'class': 'form-control'}),
            "post_graduation": forms.TextInput(attrs={'class': 'form-control'}),
            "experiance": forms.TextInput(attrs={'class': 'form-control'}),
            # "resume": forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels={
            "dob":"Date of Birth(mm/dd/yy)",
            "experiance":"Experiance(in months)"
        }