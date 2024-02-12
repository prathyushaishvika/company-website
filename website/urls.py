from django.urls import path
from.import views 
app_name='websiteapp'

urlpatterns=[
    path('',views.main,name='main'),
    path('master/',views.master,name='master'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('client',views.client,name='client'),
    path('careers',views.careers,name='careers')
]