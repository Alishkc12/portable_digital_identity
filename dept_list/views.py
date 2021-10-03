from django.shortcuts import render,redirect





# Create your views here.


from django import forms


# Create your views here.
from .models import Dept_list





def index(request):
	
	if request.user.is_authenticated:
		if request.user.is_hseb == True:
			return redirect('/hseb/')
		elif request.user.is_tu == True:
			return redirect('/tribhuwan_university/')
		elif request.user.is_superuser:
			return redirect('/admin')		
	data=Dept_list.objects.all();
	mydata={ 
	'data':data
	}
	return render(request,'index.html',context=mydata)



