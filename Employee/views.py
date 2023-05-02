from imaplib import _Authenticator
from multiprocessing import context
from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Datas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required
def home(request): #127.0.0.1:8000/addData
    mydata = Datas.objects.all()
    if(mydata != ''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
    
@login_required
def addData(request):
    if request.method == 'POST':
        emp_no = request.POST['emp_no']
        name = request.POST['name']
        address = request.POST['address']
        emp_start_date = request.POST['emp_start_date']
        emp_end_date = request.POST['emp_end_date']
        status = request.POST['status']

        obj = Datas()
        obj.Emp_no = emp_no
        obj.Name = name
        obj.Address = address
        obj.Emp_start_date = emp_start_date
        obj.Emp_end_date = emp_end_date
        obj.Status = status
        obj.save()  #for storing datas on database

        mydata = Datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

@login_required
def updateData(request,id):   #127.0.0.1:8000/updateData
    mydata=Datas.objects.get(id=id)
    if request.method=='POST':
        emp_no = request.POST['emp_no']
        name = request.POST['name']
        address = request.POST['address']
        #emp_start_date = request.POST['emp_start_date']
        #emp_end_date = request.POST['emp_end_date']
        status = request.POST['status']

        mydata.Emp_no=emp_no
        mydata.Name=name
        mydata.Address=address
        #mydata.Emp_start_date=emp_start_date
        #mydata.Emp_end_date=emp_end_date
        mydata.Status=status
        mydata.save()
        return redirect('home')

    return render(request,'update.html',{'data':mydata})

@login_required  
def deleteData(request,id):  #127.0.0.1:8000/deleteData/id
    mydata=Datas.objects.get(id=id)  #object(4)
    mydata.delete()
    return redirect('home')

