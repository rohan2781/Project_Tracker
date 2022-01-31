from django.shortcuts import render,redirect,HttpResponse
from project.models import Project
from django.contrib.auth.decorators import login_required
from project.forms import ProjectRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def project(request):
    if not request.user.is_authenticated:
        messages.info(request,'Please login first')
        return redirect('/login')
    else:
        return render(request,'project.html')

def newProject(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectRegistrationForm(request.POST)
            context = {'form': form}
            if form.is_valid():
                form.save()
                created = True
                form = ProjectRegistrationForm()
                context = {
                    'created': created,
                    'form': form,
                }
                return render(request, 'new_project.html', context)
            else:
                return render(request, 'new_project.html', context)
        else:
            form = ProjectRegistrationForm()
            context = {
                'form': form,
            }
    else:
        messages.info(request,'Login Required')
        return render(request,'login.html')

    return render(request,'new_project.html', context)
