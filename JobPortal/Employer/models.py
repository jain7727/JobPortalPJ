from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.




class Job(models.Model):
    JOB_TYPE=(
        ("part-time","part-time"),
        ("full-time","full=time"),
        ("internship","internship")
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    # website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)

    def _str_(self):
        return self.title


