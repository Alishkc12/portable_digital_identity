from django.contrib import admin

# Register your models here.
from .models import Dept_list,hseb_dept

# Register your models here.
admin.site.register([Dept_list,hseb_dept])