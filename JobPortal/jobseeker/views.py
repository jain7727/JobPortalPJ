from django.shortcuts import render,redirect
from jobseeker.models import MyUser,Applicant,Profile
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

#  --------------------------------------------------------------------------------------------------------------------
class HomePage(TemplateView):
    template_name = "home.html"

class ProfileCreateView(CreateView):
    model = Profile
    form_class = forms.ProfileAddForm
    template_name = "profileadd.html"
    success_url = reverse_lazy("profileadd")

class ViewProfile(ListView):
    model = Profile
    template_name = "viewprofile.html"
    context_object_name = "profiles"

