from django.urls import path
from .import  views

urlpatterns=[
	path('',views.profile),
     path('hseb_register/',views.hseb_register.as_view(), name='hseb_register'),
     path('login_hseb/',views.login_hseb, name='hseb_login'),
     path('logout/',views.logout_view, name='logout'),
     path('profile/',views.profile, name='profile'),
     path('test/',views.test, name='test'),
]