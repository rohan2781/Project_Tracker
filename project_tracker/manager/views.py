from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from home.models import Client
from .models import Developer
from home.forms import ClientRegistration,DevRegistration
from django.contrib import messages
from django.contrib.auth.models import User, auth

def manager(request):
    if request.user.is_authenticated:
        data = User.objects.all()
        return render(request,'admin.html',{'data':data})
    else:
        return redirect('/login')
# Create your views here.
def admin_client(request):
    if request.user.is_authenticated:
        client = User.objects.all()
        return render(request,'client.html',{'client':client})
    else:
        return redirect('/login')

def developer(request):
    if request.user.is_authenticated:
        developer = Developer.objects.all()
        return render(request,'view_developers.html',{'developer':developer})
    else:
        return redirect('/login')

def remove_developer(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Developer.objects.get(pk=id)
            pi.delete()
            messages.info(request,"Deleted Successfully")
            return redirect('/manager/view_developers')
        else:
            pi=Developer.objects.get(pk=id)
        developer = Developer.objects.get(pk=id)
        return render(request,'remove_developer.html',{'developer':developer})
    else:
        return redirect('/login')

def update_developer(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Developer.objects.get(pk=id)
            temp=pi.email
            developer = DevRegistration(request.POST, instance=pi)
            if developer.is_valid():
                if request.POST['email']==temp:
                    developer.save()
                    messages.info(request,"Updated Succesfully")
                    return redirect('/manager/view_developers')
                else:
                    messages.info(request,"Can't Change Email")
        pi = Developer.objects.get(pk=id)
        developer = DevRegistration(instance=pi)
        return render(request,'update_developer.html',{'form':developer})
    else:
        return redirect('/login')
