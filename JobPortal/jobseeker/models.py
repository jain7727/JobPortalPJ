from django.db import models
from Employer.models import Job
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, role,username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, role,username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=role,
            username=username


        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email=models.EmailField(max_length=25,unique=True)
    options=(("jobseeker","jobseeker"),("employer","employer"))
    role=models.CharField(max_length=25,choices=options,default="jobseeker",blank=True,null=True)
    username=models.CharField(max_length=50)
    is_active =models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    object=MyUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['username','role']

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    user = models.CharField(max_length=120)
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
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    jobs=models.ForeignKey(Job,on_delete=models.CASCADE,null=True)
    user=models.CharField(max_length=120)

    created=models.CharField(max_length=120)
    options=(("apply","apply"),
             ("cancelled","cancelled"))

    status=models.CharField(max_length=80,choices=options,default="apply")
    active_status=models.BooleanField(default=True)



