from django.shortcuts import render , redirect
from django.core.mail import send_mail
from test_project import settings
from django.http import HttpResponse
from .models import Customer

#Create your views here.

def homepageview(request):
    return render(request,'home.html')


def add_detail(request):
    firstname1=request.POST["firstname1"]
    lastname1=request.POST["lastname1"]
    
    detailinfo = Customer(firstname=firstname1,lastname=lastname1)
    detailinfo.save()
    if request.method == 'POST':
        message = request.POST['firstname1']

        send_mail('Contact', message, settings.EMAIL_HOST_USER, ['chikku29990@gmail.com'],fail_silently=False)

    return render(request, 'test.html')