from django.shortcuts import render,HttpResponse

def index(request):
    return render (request,'index.html')
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if (username=="admin" and password=="admin01"):
            return render(request,'admin.html')
        elif(username=="customer" and password=="customer01"):
            return render(request,'project.html')
        elif(username=="#" or password=="#"):
            return HttpResponse("Hello")

    return render(request,'login.html')

def admin(request):
    return render(request,'admin.html')

def customer(request):
    return render(request,'project.html')
