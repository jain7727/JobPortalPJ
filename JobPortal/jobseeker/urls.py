from django.urls import path
from jobseeker import views

#  git token  :  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

urlpatterns=[
    path("home",views.HomePage.as_view(),name="home"),
    path("accounts/userregistration",views.UserRegistrationView.as_view(),name="signup"),
    path("accounts/userlogin",views.UserSigninView.as_view(),name="userlogin"),
    path("accounts/userlogout",views.user_signout,name="userlogout"),
    path("profile/profileadd",views.ProfileCreateView.as_view(),name="profileadd"),
    path("profile/viewprofile",views.ViewProfile.as_view(),name="viewprofile"),
    path("profile/viewprofile/details/<int:pk>",views.ProfileDetailView.as_view(),name="profiledetails"),
    path("profile/viewprofile/editprofile/<int:pk>",views.ProfileUpdateView.as_view(),name="editprofile"),
    path("jobs/listalljobs",views.ListAllJobs.as_view(),name="listalljobs"),
    path("jobs/listalljobs/jobdetails/<int:pk>",views.JobDetailView.as_view(),name="jobdetails")
]