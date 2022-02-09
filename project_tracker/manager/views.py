from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from home.models import Client
from .models import Developer
from home.forms import ClientRegistration
from django.contrib import messages


def manager(request):
        data = Client.objects.all()
        return render(request,'admin.html',{'data':data})
# Create your views here.
def admin_client(request):
    client = Client.objects.all()
    return render(request,'client.html',{'client':client})

def developer(request):
    developer = Developer.objects.all()
    return render(request,'view_developers.html',{'developer':developer})

def remove_developer(request,id):
    if request.method == "POST":
        pi = Developer.objects.get(pk=id)
        pi.delete()
        messages.info(request,"Deleted Successfully")
        return redirect('/manager/view_developers')
    else:
        pi=Developer.objects.get(pk=id)
    developer = Developer.objects.get(pk=id)
    return render(request,'remove_developer.html',{'developer':developer})

def update_developer(request,id):
    if request.method == 'POST':
        pi = Developer.objects.get(pk=id)
        temp=pi.email
        developer = ClientRegistration(request.POST, instance=pi)
        if developer.is_valid():
            if request.POST['email']==temp:
                developer.save()
                messages.info(request,"Updated Succesfully")
                return redirect('/manager/view_developers')
            else:
                messages.info(request,"Can't Change Email")
    pi = Developer.objects.get(pk=id)
    developer = ClientRegistration(instance=pi)
    return render(request,'update_developer.html',{'form':developer})
