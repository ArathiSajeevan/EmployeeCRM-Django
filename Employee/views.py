from django.http import HttpResponse
from django.shortcuts import render
from .models import Datas

# Create your views here.

def home(request):

    if request.method == 'POST':
        emp_no = request.POST['emp_no']
        name = request.POST['name']
        address = request.POST['address']
        emp_start_date = request.POST['emp_start_date']
        emp_end_date = request.POST['emp_end_date']
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
    return render(request,'home.html')

