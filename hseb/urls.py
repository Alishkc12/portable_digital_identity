from django.urls import path
from .import  views

urlpatterns=[
	path('',views.profile),
     path('hseb_register/',views.hseb_register.as_view(), name='hseb_register'),
     path('login_hseb/',views.login_hseb, name='hseb_login'),
     path('logout/',views.logout_view, name='logout'),
     path('profile/',views.profile, name='profile'),
     path('class_12/',views.class_12, name='class_12'),
     path('class_11/',views.class_11, name='class_11'),
     path('class_11_mgmt/',views.class_11_mgmt, name='class_11_mgmt'),
     path('class_12_mgmt/',views.class_12_mgmt, name='class_12_mgmt'),
     path('profile/2_science/',views.class_11_12_science, name='test1'),
     path('2_science/',views.class_11_12_science, name='test1'),
     path('2_mgmt/',views.class_11_12_mgmt, name='test2'),
     path('profile/2_mgmt/',views.class_11_12_mgmt, name='test2'),
     path('details/',views.details, name= 'view_student_details'), 
    
]