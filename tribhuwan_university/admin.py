from django.contrib import admin

# Register your models here.
from .models import dept_tu,csit_subj1,student_main_tu

# Register your models here.
admin.site.register([dept_tu,csit_subj1,student_main_tu])