from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from home.models import Client
from manager.models import Developer
import datetime as dt
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your views here.

def project(request,id):
    if request.user.is_authenticated:
        project=Project.objects.get(pk=id)
        dev=Developer.objects.all()
        feeds=Comment.objects.filter(p_id=project.id)
        repli=Reply.objects.all()
        pro=project.developer.split(',')
        pro2=[]
        for i in pro:
            for j in dev:
                if i==j.email:
                    pro2.append(j.first_name + ' - ' + j.last_name)
        dev=pro2
        client=User.objects.get(email=project.person)
        if request.method == 'POST':
            if request.POST['sub']=='Submit':
                feed=request.POST['feed']
                first=request.user.username
                last=request.user.last_name
                if(first=='admin'):
                    comments=Comment(feed=feed,p_id=project.id,name='Admin')
                else:
                    comments=Comment(feed=feed,p_id=project.id,name=first+' '+last)
                comments.save()
            elif request.POST['sub']=='Reply':
                l=''
                m=''
                for i in feeds:
                    l+=request.POST.get('feed'+str(i.id),' ')
                    m+=request.POST.get('f'+str(i.id),' ')
                feed=l.strip()
                c_id=m.strip()
                first=request.user.username
                last=request.user.last_name
                if(first=='admin'):
                    replys=Reply(feed=feed,c_id=c_id,name='Admin')
                else:
                    replys=Reply(feed=feed,c_id=c_id,name=first+' '+last)
                replys.save()
        return render(request,'project.html',{'project':project,'client':client,'dev':dev,'feeds':feeds,'repli':repli})
    else:
        return redirect('/login')

def projects(request):
    if request.user.is_authenticated:
        client=User.objects.all()
        project=Project.objects.all()
        return render(request,'projects.html',{'project':project,'client':client})
    else:
        return redirect('/login')

def newProject(request):
    if request.user.is_authenticated:
        dev=Developer.objects.all()
        client=User.objects.all()
        if request.method == 'POST':
            form = ProjectRegistrationForm(request.POST)
            context = {'form': form,'client': client,'dev':dev}
            if form.is_valid():
                dates=request.POST['dead_line']
                dates = datetime.strptime(dates, '%Y-%m-%d')
                dates= dates.date()
                if dates < dt.date.today():
                    messages.info(request,'Date Must Of Future !')
                    return render(request, 'new_project.html', context)
                name=request.POST['name']
                if Project.objects.filter(name=name).exists():
                    messages.info(request,'Project With Same Name Already Exists !')
                    return render(request, 'new_project.html', context)
                l=request.POST.getlist('developer')
                str=''
                for i in l:
                    str=str+i+','
                if len(l)==0:
                    messages.info(request,'Please Select Atleast one Developer !!')
                    return render(request, 'new_project.html', context)
                if request.POST['person']=='Select':
                    messages.info(request,'Please Select A Client !!')
                    return render(request, 'new_project.html', context)
                else:
                    form.save()
                    Project.objects.filter(name=name).update(person=request.POST['person'])
                    Project.objects.filter(name=name).update(developer=str)
                    created = True
                    form = ProjectRegistrationForm()
                    context = {'created': created,'form': form,'client': client,'dev':dev}
                    return render(request, 'new_project.html', context)
            else:
                messages.info(request,'Date Error In Form')
                return render(request, 'new_project.html', context)
        else:
            form = ProjectRegistrationForm()
            context = { 'form': form,'client': client,'dev':dev}
        return render(request,'new_project.html',context)
    else:
        return redirect('/login')


def remove_project(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Project.objects.get(pk=id)
            pi.delete()
            messages.info(request,"Deleted Successfully")
            return redirect('/project/projects')
        else:
            pi=Project.objects.get(pk=id)
        project = Project.objects.get(pk=id)
        return render(request,'remove_project.html',{'project':project})
    else:
        return redirect('/login')

# for Updating client information
def update_project(request,id):
    if request.user.is_authenticated:
        client=User.objects.all()
        dev=Developer.objects.all()
        if request.method == 'POST':
            pi = Project.objects.get(pk=id)
            temp=pi.name
            project = ProjectRegistrationForm(request.POST, instance=pi)
            if project.is_valid():
                dates=request.POST['dead_line']
                dates = datetime.strptime(dates, '%Y-%m-%d')
                dates= dates.date()
                if request.POST['name']!=temp:
                        messages.info(request,'Project With Same Name Already Exists !')
                elif dates < dt.date.today():
                    messages.info(request,'Date Must Of Future !')
                else:
                    project.save()
                    if request.POST['person']!='set':
                        Project.objects.filter(id=pi.id).update(person=request.POST['person'])
                    messages.info(request,"Updated Succesfully")
                    l=request.POST.getlist('developer')
                    str=''
                    for i in l:
                        str=str+i+','
                    Project.objects.filter(id=pi.id).update(developer=str)
                    return redirect('/project/projects')
        pi = Project.objects.get(pk=id)
        pro=pi.person
        pro1=pi.developer
        pro1=pro1.split(',')
        for i in client:
            if i.email==pro:
                pro=i.username + ' - ' + i.last_name
        for i in pro1:
            for j in dev:
                if j.email==i:
                    j.password='set'
        project = ProjectRegistrationForm(instance=pi)
        return render(request,'update_project.html',{'form':project,'client':client,'pro':pro,'dev':dev})
    else:
        return redirect('/login')