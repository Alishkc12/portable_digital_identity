from django.contrib import admin

# Register your models here.
from .models import dept_hseb,student_main

# Register your models here.
admin.site.register([dept_hseb,student_main])