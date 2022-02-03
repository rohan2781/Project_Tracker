from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from home.models import Client

def manager(request):
        data = Client.objects.all()
        return render(request,'admin.html',{'data':data})
# Create your views here.
def admin_client(request):
    client = Client.objects.all()
    return render(request,'client.html',{'client':client})
