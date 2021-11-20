from django.urls import path
from .import  views

urlpatterns=[
	path('',views.profile),
     path('tribhuwan_university_register/',views.tribhuwan_university_register.as_view(), name='tribhuwan_university_register'),
     path('login_tribhuwan_university/',views.login_tribhuwan_university, name='tribhuwan_university_login'),
     path('logout/',views.logout_view, name='logout'),
     path('profile/',views.profile, name='profile'),
     path('profile/bsc_csit/',views.csit, name='csit'),
     path('bsc_csit/',views.csit, name='csit'),
     path('class_csit/',views.class_csit, name='class_csit'),
     path('details/',views.details, name= 'view_student_details_tu'),
  
]