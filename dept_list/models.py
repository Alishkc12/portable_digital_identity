from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .helpers import *


    

class Dept_list(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/dept1')
    slug = models.SlugField(max_length=150,null = True, blank=True)
    TYPES = (
        ('education', 'education'),
        ('transportation', 'transportation'),
        ('health', 'health'),
        ('security', 'security'),
        ('online_form', 'online_form'),
        ('online_verify', 'online_verify'),
    )
    category = models.CharField(max_length=30, choices=TYPES,default="")

    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Dept_list, self).save(*args, **kwargs)   

    def __str__(self):
        return self.name     




