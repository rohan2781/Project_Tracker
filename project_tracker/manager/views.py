from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from home.models import Client
from .models import Developer
from home.forms import ClientRegistration,DevRegistration
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import EmailMessage
from project.models import Project
import datetime as dt

def manager(request):
    if request.user.is_authenticated:
        project = Project.objects.all()
        j = 0
        for i in project:
            if i.dead_line < dt.date.today():
                j += 1
        developer = Developer.objects.all()
        data = User.objects.all().exclude(username='admin')
        return render(request,'dashboard.html',{'data':data, 'developer':developer, 'project':project, 'completed_project':j})
    else:
        return redirect('/login')
# Create your views here.
def admin_client(request):
    if request.user.is_authenticated:
        client = User.objects.all().exclude(username='admin')
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
            temp = pi.email
            email = EmailMessage(
            'Account removed Successfully',
            'Your position as Django developer from PTS has been removed.',
            'noreply@semycolon.com',
            [temp],
            )
            email.send(fail_silently = False)
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
                    username = developer.cleaned_data['first_name']
                    last_name = developer.cleaned_data['last_name']
                    email = developer.cleaned_data['email']
                    password = developer.cleaned_data['password']
            if request.POST['email']==temp:
#                    email_subject = 'Account information updated'
#                    email_body='Thank you!! for regestering with PTS.\n\nYour updated credentials are,\nfirst_name: %s\nlast_name: %s\nemail: %s\npassword: %s' % (username,last_name,email,password,)
                    email = EmailMessage(
                    'Account information updated',
                    'Your updated credentials are,\n\nfirst_name: %s\nlast_name: %s\nemail: %s\npassword: %s' % (username,last_name,email,password,),
                    'noreply@semycolon.com',
                    [temp],
                    )
                    email.send(fail_silently = False)
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
