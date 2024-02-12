from django.shortcuts import render
from.models import *


# Create your views here.

def login(request):
    return render (request,'company/login.html')

# def dashboard(request):
#     return render (request,'company/dashboard.html')

def dashboard(request):
    applicants = Candidate.objects.all()
    return render(request, 'dashboard.html', {'applicants': applicants})