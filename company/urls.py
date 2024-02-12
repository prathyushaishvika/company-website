from django.urls import path
from.import views 
app_name='companyapp'

urlpatterns=[
    path('',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    
]
