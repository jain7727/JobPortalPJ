from django.shortcuts import render,redirect
from Employer.models import Job
from Employer.forms import JobCreationForm,JobSearchForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from django.views.generic.edit import DeleteView


# Create your views here.

class JobCreationView(CreateView):
    model = Job
    form_class=JobCreationForm
    template_name="jobform.html"
    success_url=reverse_lazy("jobform")

    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context["jobdescription"]=self.model.objects.all()
    #     return context


class JobListView(ListView):
    model = Job
    form_class=JobCreationForm
    template_name="joblist.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["jobdescriptions"]=self.model.objects.filter(active_status=True)
        return context

class JobSeekersJobListView(ListView):
    model=Job
    form_class = JobSearchForm
    form_class=JobCreationForm
    template_name="alljobsforyou.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["jobdescriptions"]=self.model.objects.all()
        return context


class JobEditView(UpdateView):
    model=Job
    form_class=JobCreationForm
    template_name="jobsupdate.html"
    pk_url_kwarg='id'
    success_url=reverse_lazy("listjobs")

class JobDeleteView(DeleteView):
    template_name="joblist.html"
    model=Job
    pk_url_kwarg="id"
    success_url=reverse_lazy("listjobs")

    def get(self,request,*args,**kwargs):
        job=self.model.objects.get(id=kwargs["id"])
        job.active_status=False
        job.save()
        return redirect("listjobs")




# class JobSeekersJobSearchView(ListView):
#     model=Job
#     form_class=JobSearchForm
#
#     template_name="alljobsforyou.html"
#     success_url=reverse_lazy("alljobsforyou")

