from django.shortcuts import redirect,reverse,render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from project.models import Project
from .forms import ClientRegistration
from .models import Client
from manager.models import Developer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage

def index(request):
    if not request.user.is_authenticated:
        return render (request,'index.html')
    else:
        logout_view(request)
        return render (request,'index.html')
# Create your views here.

#def remove_client(request):
#    return render(request,'remove_client.html')
def logins(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                value=User.objects.get(email=email)
                username=value.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/manager')
                #if email=='admin@gmail.com':
                    #   return redirect('/manager')
                else:
                    if User.objects.filter(email=email,password=password).exists():
                        client=User.objects.get(email=email)
                        login(request, client)
                        return redirect('/account/'+str(client.id))
            else:
                messages.info(request,"Invalid Credentials")
    else:
        logout_view(request)
    return render(request,'login.html')


def client(request,id):
    if request.user.is_authenticated:
        client=User.objects.get(pk=id)
        project=Project.objects.filter(person=client.email)
        return render(request,'login_client.html',{'project':project,'client':client})
    else:
        return redirect('/login')


# For adding client
def SignUp(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
    #        id = request.POST.getlist('developer')
    #        return HttpResponse(request.POST.get('developer')+"a")
            client = ClientRegistration(request.POST)
    #        id = request.POST['id']
            if client.is_valid():
                username = client.cleaned_data['username']
                last_name = client.cleaned_data['last_name']
                email = client.cleaned_data['email']
                password = client.cleaned_data['password']
                if request.POST.get('developer') == "1":
                    if Developer.objects.filter(email=email).exists():
                        messages.info(request,"Email already taken")
                    else:
                        reg = Developer(first_name=username, last_name=last_name, email=email, password=password)
                        reg.is_activate=False
                        email_subject = 'Position Assigned!'
                        email_body="Congrats!! You are now registered as a Django developer with PTS."
                        email = EmailMessage(
                        email_subject,
                        email_body,
                        'noreply@semycolon.com',
                        [email],
                        )
                        email.send(fail_silently = False)
                        reg.save()
                        messages.info(request,'Developer Added Successfully')
                        return redirect('/sign-up/')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.info(request,"Email already exists")
                    elif User.objects.filter(username=username).exists():
                        messages.info(request,"Please Use Different Username")
                    else:
                        reg = User.objects.create(username=username, last_name=last_name, email=email, password=password)
                        email_subject = 'Account Registered!'
                        email_body = '''Thank you!! for regestering with PTS.

Your login credentials are,
email: %s\npassword: %s''' % (
        email,
        password,
    )
                        email = EmailMessage(
                        email_subject,
                        email_body,
                        'noreply@semycolon.com',
                        [email],
                        )
                        email.send(fail_silently = False)
                        reg.save()
                        messages.info(request,'Client Added Successfully')
                        return redirect('/sign-up/')

        else:
            client = ClientRegistration()
        return render(request,'sign_up.html',{'form':client})
    else:
        return redirect('/login')

# For removing Client
def remove_client(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = User.objects.get(pk=id)
            temp = pi.email
            project=Project.objects.filter(person=pi.email)
            email_subject = 'Account removed Successfully'
            email_body='''Your account has been deleted.
Sorry for inconvinencies you experienced with PTS, we are trying to improve. '''
            email = EmailMessage(
            email_subject,
            email_body,
            'noreply@semycolon.com',
            [temp],
            )
            email.send(fail_silently = False)
            pi.delete()
            for i in project:
                i.delete()
            messages.info(request,"Deleted Successfully")
            return redirect('/manager/client')
        else:
            pi=User.objects.get(pk=id)
        client = User.objects.get(pk=id)
        return render(request,'remove_client.html',{'client':client})
    else:
        return redirect('/login')

# for Updating client information
def update_client(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            temp=pi.email
            client = ClientRegistration(request.POST, instance=pi)
            if client.is_valid():
                if request.POST['email']==temp:
                    username = client.cleaned_data['username']
                    last_name = client.cleaned_data['last_name']
                    password = client.cleaned_data['password']
                    email_subject = 'Account information updated!'
                    email_body='''Your account information has been updated.

Your updated login credentials are,
email: %s\npassword: %s''' % (
    temp,
    password,
)
                    email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [temp],
                    )
                    email.send(fail_silently = False)
                    client.save()
                    messages.info(request,"Updated Succesfully")
                    return redirect('/manager/client')
                else:
                    messages.info(request,"Can't Change Email")
        pi = User.objects.get(pk=id)
        client = ClientRegistration(instance=pi)
        return render(request,'update_client.html',{'form':client})
    else:
        return redirect('/login')



def logout_view(request):
    logout(request)
    return redirect('/')
