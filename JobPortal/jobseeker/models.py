from django.db import models
from Employer.models import Job




# Create your models here.

class Profile(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    mobile=models.IntegerField(max_length=12)
    dob=models.DateField("mm/dd/yy",auto_now_add=False,auto_now=False,blank=True,null=True)
    options=(("male","male"),("female","female"))
    gender=models.CharField(max_length=80,choices=options,default="male")
    address=models.CharField(max_length=200,null=True)
    graduation=models.CharField(max_length=100,null=True,blank=True)
    post_graduation=models.CharField(max_length=100,null=True,blank=True)
    experiance=models.IntegerField("months")
    resume=models.FileField(upload_to="resume",null=True)



class Applicant(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    jobs=models.ForeignKey(Job,on_delete=models.CASCADE)
    user=models.CharField(max_length=25)

    created=models.CharField(max_length=25)
    options=(("apply","apply"),
             ("cancelled","cancelled"))

    status=models.CharField(max_length=80,choices=options,default="apply")
    active_status=models.BooleanField(default=True)



