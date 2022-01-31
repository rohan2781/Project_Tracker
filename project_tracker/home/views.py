from django.shortcuts import redirect,reverse,render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render (request,'index.html')
# Create your views here.

def SignUp(request):

    if request.method == "POST":
        name = request.POST['username']
        Email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if Password1 == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request,'Email_id already exist')
                return render(request,'sign_up.html')
            else:
                user = User.objects.create_user (username=name, password=Password1, email=Email)
                user.save();
                return render(request,'login.html')
        else:
            messages.info(request,"Password Didn't Matched Retry")

    return render(request,'sign_up.html')

def logins(request):
    if request.user.is_authenticated:
        if request.user.username!='Rohan2781':
            return redirect('/project')
        else:
            return redirect('/manager')
    elif request.method == 'POST':
        name = request.POST['username']
        pword = request.POST['password']
#        l=login(username=name, password=pword)
#        l.save()
#        return redirect('/project')
        user = auth.authenticate(username=name,password=pword)

        if user is not None:
            auth.login(request,user)
            if request.user.username!='Rohan2781':
                return redirect('/project')
            else:
                return redirect('/manager')
        else:
            messages.info(request,"Invalid Credentials")

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
