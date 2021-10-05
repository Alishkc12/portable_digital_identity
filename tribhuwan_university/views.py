from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User
from .form import Tribhuwan_universitySignUpForm
from django.http import HttpResponse
from .models import dept_tu


class tribhuwan_university_register(CreateView):

    model = User
    form_class = Tribhuwan_universitySignUpForm
    template_name = 'register_tribhuwan_university.html'

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/')




def login_tribhuwan_university(request):
    if request.user.is_authenticated:
        if request.user.is_tu == True:
            return redirect('/tribhuwan_university/profile')
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
                return redirect('/tribhuwan_university/login_tribhuwan_university')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login_tu.html',context={'form':AuthenticationForm()})  


def logout_view(request):
    logout(request)
    return redirect('/')


def profile(request):
    data=dept_tu.objects.all();
    
    if request.user.is_authenticated:
        if request.user.is_tu == False:
            return redirect('/')
        a=request.user.is_tu
        e=request.user
        b={'c':a,'d':e,'data':data}
        return render(request,'tribhuwan_university_profile.html',context=b) 
    else:
        return redirect('/tribhuwan_university/login_tribhuwan_university')   

    



    