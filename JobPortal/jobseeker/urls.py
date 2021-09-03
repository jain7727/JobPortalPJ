from django.urls import path
from jobseeker import views

 # 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

urlpatterns=[
    path("home",views.HomePage.as_view(),name="home"),
    path("accounts/userregistration",views.UserRegistrationView.as_view(),name="signup"),
    path("accounts/userlogin",views.UserSigninView.as_view(),name="userlogin"),
    path("accounts/userlogout",views.user_signout,name="userlogout"),
    path("profile/profileadd",views.ProfileCreateView.as_view(),name="profileadd"),
    path("profile/details",views.ViewProfile.as_view(),name="viewprofile"),
]