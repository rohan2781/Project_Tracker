from django.shortcuts import render
from django.contrib.auth.models import User, auth
from home.models import Client

def manager(request):
    if request.user.is_authenticated and request.user.username=='Rohan2781':
        return render(request,'admin.html')
# Create your views here.
def admin_client(request):
    client = Client.objects.all()
    return render(request,'admin_client.html',{'client':client})
