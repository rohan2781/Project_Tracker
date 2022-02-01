from django.shortcuts import redirect,reverse,render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ClientRegistration
from .models import Client

def index(request):
    return render (request,'index.html')
# Create your views here.

#def remove_client(request):
#    return render(request,'remove_client.html')

# For adding client
def SignUp(request):
    if request.method == 'POST':
        client = ClientRegistration(request.POST)
        if client.is_valid():
            first_name = client.cleaned_data['first_name']
            second_name = client.cleaned_data['second_name']
            email = client.cleaned_data['email']
            password = client.cleaned_data['password']
            if Client.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
            else:
                reg = Client(first_name=first_name, second_name=second_name, email=email, password=password)
                reg.save()
                messages.info(request,'Client Added Successfully')
                return redirect('/manager/admin_client')
#    if requests.method == "POST":
#        name = request.POST['username']
#        Email = request.POST['email']
#        Password1 = request.POST['password1']
#        Password2 = request.POST['password2']
#
#        if Password1 == Password2:
#            if User.objects.filter(email=Email).exists():
#                messages.info(request,'Email_id already exist')
#                return render(request,'sign_up.html')
#            else:
#                user = User.objects.create_user (username=name, password=Password1, email=Email)
#                user.save();
#                return render(request,'login.html')
#        else:
#            messages.info(request,"Password Didn't Matched Retry")
#
    else:
        client = ClientRegistration()
    return render(request,'sign_up.html',{'form':client})

# For removing Client
def remove_client(request,id):
    if request.method == "POST":
        pi = Client.objects.get(pk=id)
        pi.delete()
        return redirect('/manager/admin_client')
    else:
        pi=Client.objects.get(pk=id)
    client = Client.objects.get(pk=id)
    return render(request,'remove_client.html',{'client':client})

# for Updating client information
def update_client(request,id):
    if request.method == 'POST':
        pi = Client.objects.get(pk=id)
        client = ClientRegistration(request.POST, instance=pi)
        if client.is_valid():
            client.save()
        return redirect('/manager/admin_client')
    else:
        pi = Client.objects.get(pk=id)
        client = ClientRegistration(instance=pi)
    return render(request,'update_client.html',{'form':client})






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
