from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class dept_tu(models.Model):
    name= models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1/hseb')
    
    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name_plural = 'tu_department'    