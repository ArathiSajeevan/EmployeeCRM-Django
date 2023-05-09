from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Datas
from django.contrib.auth.decorators import login_required


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegisterForm



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


        if len(request.FILES) !=0:
            image = request.FILES['image']

        status = request.POST['status']


        obj = Datas()
        obj.Emp_no = emp_no
        obj.Name = name
        obj.Address = address
        obj.Emp_start_date = emp_start_date
        obj.Emp_end_date = emp_end_date
        obj.Image = image
        obj.Status = status
        obj.save()  #for storing datas on database
        return HttpResponse(obj)

        mydata = Datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

@login_required
def updateData(request,id):   #127.0.0.1:8000/updateData
    mydata=Datas.objects.get(id=id)
    if request.method =='POST':
        emp_no = request.POST['emp_no']
        name = request.POST['name']
        address = request.POST['address']
        emp_start_date = request.POST['emp_start_date']
        emp_end_date = request.POST['emp_end_date']
        status = request.POST['status']

        if len(request.FILES) !=0:
            image = request.FILES['image']

        mydata.Emp_no=emp_no
        mydata.Name=name
        mydata.Address=address
        mydata.Emp_start_date=emp_start_date
        mydata.Emp_end_date=emp_end_date
        mydata.Image=image
        mydata.Status=status
        mydata.save()
        print(":::::::::::::::::::::::here")
        return redirect('view_details')

    return render(request,'update.html',{'data':mydata})


@login_required
def deleteData(request,id):  #127.0.0.1:8000/deleteData/id
    mydata=Datas.objects.get(id=id)  #object(4)
    mydata.delete()
    return redirect('home')

@login_required
def view_details(request):
    mydata = Datas.objects.all()
    if(mydata != ''):
        return render(request,'view_details.html',{'datas':mydata})
    else:
        return render(request,'view_details.html')


@login_required
def full_size(request,id):
    mydata=Datas.objects.get(id=id)
    if(mydata != ''):
        return render(request,'fullsize.html',{'mydata':mydata})
    else:
        return render(request,'fullsize.html')
    

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
    



