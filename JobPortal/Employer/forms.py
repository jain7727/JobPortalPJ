from Employer.models import Job
from django.forms import ModelForm
from django import forms

class JobCreationForm(ModelForm):
    class Meta:
        model = Job
        fields=[
            "title",
            "description",
            "company_name",
            "company_description",
            "location",
            "type",
            "category",
            "created_at",
            "last_date",
        ]
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

class JobSearchForm(forms.Form):
    Job=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"})),

