from django.shortcuts import render
from django.contrib.auth.models import User, auth
def manager(request):
    if request.user.is_authenticated and request.user.username=='Rohan2781':
        return render(request,'admin.html')
# Create your views here.
