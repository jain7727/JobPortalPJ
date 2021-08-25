from django.db import models

# Create your models here.

class Applicant(models.Model):
    job=models.ForeignKey(on_delete=models.CASCADE)
    user=models.CharField(max_length=25)
    created=models.CharField(max_length=25)
    options=(("apply","apply"),("cancelled","cancelled"))
    status=models.CharField(max_length=80,choices=options,default="apply")

class Profile(models.Model):
    name=models.CharField(max_length=25)
    dob=models.IntegerField(max_length=14)
    options=(("male","male"),("female","female"),("other","other"))
    gender=models.CharField(max_length=80,choices=options,default="male")
    mobile=models.IntegerField(max_length=10)
    email=models.EmailField(max_length=25)
    resume=models.CharField(max_length=50)




