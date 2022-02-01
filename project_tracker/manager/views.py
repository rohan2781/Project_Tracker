from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from home.models import Client

def manager(request):
    if request.user.is_authenticated and request.user.username=='Rohan2781':
        data = Client.objects.all()
        display=request.POST.get('disp')
        if display=='1':
            return redirect('/sign-up',{'data':data})
        if display=='2':
            return redirect('/manager/client',{'data':data})
        if display=='3':
            return redirect('/project/new_project',{'data':data})
        return render(request,'admin.html',{'display':display,'data':data})
# Create your views here.
def admin_client(request):
    client = Client.objects.all()
    return render(request,'client.html',{'client':client})
