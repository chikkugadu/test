from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Customer

# Create your views here.

def homepageview(request):
    return render(request,'home.html')


def add_detail(request):
    firstname1=request.POST["firstname1"]
    lastname1=request.POST["lastname1"]
    
    detailinfo = Customer(firstname=firstname1,lastname=lastname1)
    detailinfo.save()
    
    return render(request, 'test.html')