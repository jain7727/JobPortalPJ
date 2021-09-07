from django.forms import ModelForm
from django import forms
from jobseeker.models import MyUser,Profile,Applicant
from Employer.models import Job
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

#  ------------------------------ USER DETAILS ------------------------------------------------------------------------

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

#  --------------------------- JOB PROFILE ----------------------------------------------------------------------------

class JobDetailForm(ModelForm):
    class Meta:
        model = Job
        fields=["title","description","company_name","company_description","location","type","category","created_at",
            "last_date",]

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "company_name":forms.TextInput(attrs={"class":"form-control"}),
            "company_description":forms.Textarea(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "type":forms.Select(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
            "created_at":forms.DateTimeInput(attrs={"class":"form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control"}),
        }