from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_tu = models.BooleanField(default=False)
    is_hseb = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class tribhuwan_university(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=20,default="")
    citizenship_no = models.CharField(max_length=20 ,default="")


    class Meta:
        
        verbose_name_plural = 'tribhuwan_university'
    def __str__(self):
        return self.address   




class HSEB(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=20,default="")
    citizenship_no = models.CharField(max_length=20, default="")

    class Meta:
        
        verbose_name_plural = 'HSEB'
    def __str__(self):
        return self.phone_number  


class Citizen(models.Model):
    name=models.CharField(max_length=100)
    citizenship_no=models.CharField(max_length=100,unique=True) 
    birthplace=models.CharField(max_length=100,default="")
    img = models.ImageField(upload_to='static/img/dept1/student_hseb',default="")

    from datetime import datetime

    date = models.DateField(default=datetime.now)

    mothers_name=models.CharField(max_length=100,default="")
    fathers_name=models.CharField(max_length=100,default="")
    spouse_name=models.CharField(max_length=100,default="",null=True,blank=True)
    district=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    ward_no=models.CharField(max_length=100,default="")
    gender=models.CharField(max_length=100,default="")
    nagrita_date=  models.DateField(default=datetime.now)


    def __str__(self):
        return self.citizenship_no       












        
       
