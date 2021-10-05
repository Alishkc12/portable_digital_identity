from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView

from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User
from .form import HSEBSignUpForm
from django.http import HttpResponse
from .models import dept_hseb


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



def test(request):
    return render(request,'dept_citizen.html')

    