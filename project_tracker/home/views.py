from django.shortcuts import redirect, render,HttpResponse
from home.models import login
def index(request):
    return render (request,'index.html')
# Create your views here.

def logins(request):
    if request.method == 'POST':
        name = request.POST['username']
        pword = request.POST['password']
        l=login(username=name, password=pword)
        l.save()
        return redirect('/project')
    return render(request,'login.html')

def admin(request):
    return render(request,'admin.html')

def customer(request):
    return render(request,'project.html')
