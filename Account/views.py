
from imaplib import _Authenticator
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    template_name="login/login.html"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    #cus_user = User.objects.filter(username=username).exists()
    #if cus_user:
        #custome_user = User.objects.get(username=username)
        #if custome_user.is_active == False:
            #messages.success(request, 'This User is Inactive.', 'alert-danger')
            #return render(request, template_name, context)
    

        
    #user = _Authenticator(request, username=username, password=password)

    return render(request,template_name)
    
