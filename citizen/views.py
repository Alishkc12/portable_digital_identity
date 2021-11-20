from django.shortcuts import render,redirect





# Create your views here.


from django import forms


# Create your views here.
from .models import Dept_list_citizen





def index(request):
	
			
	data=Dept_list_citizen.objects.all();
	mydata={ 
	'data':data
	}
	return render(request,'index_citizen.html',context=mydata)




def bank(request):
	
	
	return render(request,'new_bank_acc.html')


def liscence(request):
	
	
	return render(request,'liscence_form.html')
