from django.shortcuts import redirect,reverse,render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render (request,'index.html')
# Create your views here.

def SignUp(request):

    if request.method == "POST":
        CompanyName = request.POST['Company_Name']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if Password1 == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request,'Email_id already exist')
                return render(request,'sign_up.html')
            else:
                user = User.objects.create_user (username=CompanyName, password=Password1, email=Email)
                user.save();
                return render(request,'login.html')
        else:
            messages.info(request,"Password not matching")
            return render(request,'sign_up.html')

    return render(request,'sign_up.html')

def logins(request):
    if request.method == 'POST':
        name = request.POST['username']
        pword = request.POST['password']
#        l=login(username=name, password=pword)
#        l.save()
#        return redirect('/project')
        user = auth.authenticate(username=name,password=pword)

        if user is not None:
            auth.login(request,user)
            return render(request,'project.html')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def customer(request):
    return render(request,'project.html')
