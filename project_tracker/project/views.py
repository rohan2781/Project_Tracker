from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectRegistrationForm
from home.models import Client
# Create your views here.

def project(request):
    if not request.user.is_authenticated:
        messages.info(request,'Please login first')
        return redirect('/login')
    else:
        return render(request,'project.html')

def projects(request):
    if not request.user.is_authenticated:
        messages.info(request,'Please login first')
        return redirect('/login')
    else:
        project=Project.objects.all()
        return render(request,'projects.html',{'project':project})

def newProject(request):
    #if request.user.is_authenticated:
    client=Client.objects.all()
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            name=request.POST['name']
            if Project.objects.filter(name=name).exists():
                messages.info(request,'Project With Same Name Already Exists !')
                return render(request, 'new_project.html', context)
            else:    
                form.save()
                created = True
                form = ProjectRegistrationForm()
                context = {'created': created,'form': form,}
                return render(request, 'new_project.html', context)
        else:
            return render(request, 'new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = { 'form': form,'client': client}
    return render(request,'new_project.html',context)
