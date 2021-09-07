from django.shortcuts import render,redirect
from jobseeker.models import MyUser,Applicant,Profile
from Employer.models import Job
from django.views.generic import CreateView,UpdateView,TemplateView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from jobseeker import forms

# Create your views here.

class UserRegistrationView(CreateView):
    model = MyUser
    template_name = "registration.html"
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy("userlogin")

class UserSigninView(TemplateView):
    template_name = "userlogin.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=forms.UserSigninForm()
        return context

    def post(self, request, *args, **kwargs):
        form=forms.UserSigninForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.role=="jobseeker":
                    return redirect("profileadd")
                else:
                    return redirect("home")
            else:
                return render(request,self.template_name,{'form':form})

def user_signout(request):
    logout(request)
    return redirect("userlogin")

#  ----------------------------------------- Profile ------------------------------------------------------------------

class HomePage(TemplateView):
    template_name = "home.html"

class ProfileCreateView(CreateView):
    model = Profile
    template_name = "profileadd.html"
    form_class = forms.ProfileAddForm

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            timesheet=form.save(commit=False)
            timesheet.user=request.user
            timesheet.save()
            return redirect("home")

class ViewProfile(ListView):
    model = Profile
    template_name = "viewprofile.html"
    context_object_name = "profiles"
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "detailprofile.html"
    context_object_name = "profile"

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = forms.ProfileAddForm
    template_name = "updateprofile.html"
    success_url = reverse_lazy("viewprofile")

#  -------------------------------------------------- JOB PROFILE ------------------------------------------------------

class ListAllJobs(ListView):
    model = Job
    template_name = "listalljobs.html"
    context_object_name = "jobs"

class JobDetailView(DetailView):
    model = Job
    template_name = "jobdetailview.html"
    context_object_name = "job"

class JobUserProfileUpdateView(UpdateView):
    model = Profile
    form_class = forms.ProfileAddForm
    template_name = "updateprofile.html"