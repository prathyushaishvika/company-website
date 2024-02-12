from django.shortcuts import render,redirect
from.models import *

from .forms import CandidateForm
from .models import Candidate


# Create your views here.


def main(request):
    return render (request,'website/main.html')

def master(request):
    return render(request,'website/master.html')

def about(request):
    return render(request,'website/about.html')

def service(request):
    return render(request,'website/service.html')

def contact(request):
    return render(request,'website/contact.html')

def register(request):
    return render(request,'website/register.html')

def client(request):
    return render(request,'website/client.html')

def careers(request):
    return render(request,'website/careers.html')


def register(request):

    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company:dashboard')
    else:
        form = CandidateForm()
    
    return render(request,'website/register.html')



