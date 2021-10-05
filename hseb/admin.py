from django.contrib import admin

# Register your models here.
from .models import dept_hseb,student_main,student_marks_eleven,student_marks_twelve

# Register your models here.
admin.site.register([dept_hseb,student_main,student_marks_eleven,student_marks_twelve])