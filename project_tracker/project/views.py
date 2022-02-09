from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectRegistrationForm
from home.models import Client
import datetime as dt
from datetime import datetime
# Create your views here.

def project(request,id):
    project=Project.objects.get(pk=id)
    client=Client.objects.get(email=project.person)
    return render(request,'project.html',{'project':project,'client':client})

def projects(request):
    client=Client.objects.all()
    project=Project.objects.all()
    return render(request,'projects.html',{'project':project,'client':client})

def newProject(request):
    #if request.user.is_authenticated:
    client=Client.objects.all()
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form,'client': client}
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
            if request.POST['person']=='Select':
                messages.info(request,'Please Select A Client !!')
                return render(request, 'new_project.html', context)
            else:    
                form.save()
                Project.objects.filter(name=name).update(person=request.POST['person'])
                created = True
                form = ProjectRegistrationForm()
                context = {'created': created,'form': form,'client': client}
                return render(request, 'new_project.html', context)
        else:
            messages.info(request,'Date Error In Form')
            return render(request, 'new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = { 'form': form,'client': client}
    return render(request,'new_project.html',context)


def remove_project(request,id):
    if request.method == "POST":
        pi = Project.objects.get(pk=id)
        pi.delete()
        messages.info(request,"Deleted Successfully")
        return redirect('/project/projects')
    else:
        pi=Project.objects.get(pk=id)
    project = Project.objects.get(pk=id)
    return render(request,'remove_project.html',{'project':project})

# for Updating client information
def update_project(request,id):
    client=Client.objects.all()
    if request.method == 'POST':
        pi = Project.objects.get(pk=id)
        temp=pi.name
        project = ProjectRegistrationForm(request.POST, instance=pi)
        if project.is_valid():
            
            dates=request.POST['dead_line']
            dates = datetime.strptime(dates, '%Y-%m-%d')
            dates= dates.date()
            name=request.POST['name']
            if request.POST['name']!=temp:
                    messages.info(request,'Project With Same Name Already Exists !')
            elif dates < dt.date.today():
                messages.info(request,'Date Must Of Future !')

            else:
                project.save()
                if request.POST['person']!='set':
                    Project.objects.filter(id=pi.id).update(person=request.POST['person'])
                messages.info(request,"Updated Succesfully")
                return redirect('/project/projects')
    pi = Project.objects.get(pk=id)
    pro=pi.person
    for i in client:
        if i.email==pro:
            pro=i.first_name + ' - ' + i.last_name
    project = ProjectRegistrationForm(instance=pi)
    return render(request,'update_project.html',{'form':project,'client':client,'pro':pro})