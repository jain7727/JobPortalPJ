from django.urls import path
from Employer import views
urlpatterns=[
    path("jobform/",views.JobCreationView.as_view(),name="jobform"),
    path("listjobs/",views.JobListView.as_view(),name="listjobs"),
    path("jobsupdate<int:id>",views.JobEditView.as_view(),name="jobsupdate"),
    path("jobsdelete<int:id>",views.JobDeleteView.as_view(),name="jobsdelete"),
    path("alljobsforyou/",views.JobSeekersJobListView.as_view(),name="alljobsforyou"),
    path("employer/login",views.UserSigninView.as_view(),name="login"),
    path("employer/logout",views.user_logout,name="logout")


]