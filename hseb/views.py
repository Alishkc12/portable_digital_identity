from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .models import student_main
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User
from .form import HSEBSignUpForm
from django.http import HttpResponse
from .models import dept_hseb,science_class_12,science_class_11,mgmt_class_11,mgmt_class_12


class hseb_register(CreateView):

    model = User
    form_class = HSEBSignUpForm
    template_name = 'register_hseb.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/')

def login_hseb(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == True:
            return redirect('/hseb/profile')
        else:
            messages.error(request,"sorry you are not authorized") 
            


    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/hseb/login_hseb')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login_hseb.html',context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
    data=dept_hseb.objects.all();
    
    
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')
        a=request.user.is_hseb
        e=request.user
        b={'c':a,'d':e, 'data':data}
        return render(request,'hseb_profile.html',context=b) 
    else:
        return redirect('/hseb/login_hseb')      



def class_12(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')

        data=science_class_12.objects.all();
        mydata={ 
        'data':data
        }
        return render(request,'dept_citizen.html',context=mydata)



def class_11(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')


        data=science_class_11.objects.all();
        mydata={ 
        'data':data
        }
        return render(request,'dept_citizen.html',context=mydata)

def class_11_mgmt(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')


        data=mgmt_class_11.objects.all();
        mydata={ 
        'data':data
        }
        return render(request,'dept_citizen.html',context=mydata)   

def class_12_mgmt(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')


        data=mgmt_class_12.objects.all();
        mydata={ 
        'data':data
        }
        return render(request,'dept_citizen.html',context=mydata)                
        



def class_11_12_science(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')

       
        return render(request,'hseb_11_12.html')

def class_11_12_mgmt(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')

       
        return render(request,'hseb_11_12_mgmt.html')        


def details(request):
    if request.user.is_authenticated:
        if request.user.is_hseb == False:
            return redirect('/')

        data=student_main.objects.all();
        mydata={ 
        'data':data
        }
        return render(request,'student_details.html',context=mydata)