from django.contrib import admin

# Register your models here.

from jobseeker.models import Profile,Applicant
admin.site.register(Profile)
admin.site.register(Applicant)
