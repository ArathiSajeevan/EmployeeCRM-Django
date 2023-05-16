from django.shortcuts import redirect, render
from Account.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from .models import EmployeeDatas

# Create your views here.


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteData(request,id):  #127.0.0.1:8000/deleteData/id
    mydata=EmployeeDatas.objects.get(id=id)  #object(4)
    mydata.delete()
    return redirect('home')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_details(request):
    mydata = EmployeeDatas.objects.all()
    if(mydata != ''):
        return render(request,'view_details.html',{'datas':mydata})
    else:
        return render(request,'view_details.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def full_size(request,id):
    mydata=EmployeeDatas.objects.get(id=id)
    if(mydata != ''):
        return render(request,'fullsize.html',{'mydata':mydata})
    else:
        return render(request,'fullsize.html')
    

def admin_logout(request):
    logout(request)
    return redirect('/')


#form method
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    context = {}
    context['form'] = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            employeedatas = EmployeeDatas(
                Emp_no=form.cleaned_data['emp_no'], 
                Name=form.cleaned_data['name'], 
                Address=form.cleaned_data['address'], 
                Emp_start_date=form.cleaned_data['emp_start_date'], 
                Emp_end_date=form.cleaned_data['emp_end_date'], 
                Image=form.cleaned_data.get("image"),
                Status=form.cleaned_data['status'],
                )
            employeedatas.save()
            form = RegisterForm()
            return render(request, "register.html",{
                "form" : form
            })
    
    else:
        form = RegisterForm()
        return render(request, 'register.html',{
            "form" : form
    })





# @login_required
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def addData(request):
#     if request.method == 'POST':
#         emp_no = request.POST['emp_no']
#         name = request.POST['name']
#         address = request.POST['address']
#         emp_start_date = request.POST['emp_start_date']
#         emp_end_date = request.POST['emp_end_date']


#         if len(request.FILES) !=0:
#             image = request.FILES['image']

#         status = request.POST['status']


#         obj = Datas()
#         obj.Emp_no = emp_no
#         obj.Name = name
#         obj.Address = address
#         obj.Emp_start_date = emp_start_date
#         obj.Emp_end_date = emp_end_date
#         obj.Image = image
#         obj.Status = status
#         obj.save()  #for storing datas on database
#         return HttpResponse(obj)

#         mydata = Datas.objects.all()
#         return redirect('home')
#     return render(request,'home.html')

# @login_required
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def updateData(request,id):   #127.0.0.1:8000/updateData
#     mydata=Datas.objects.get(id=id)
#     if request.method =='POST':
#         emp_no = request.POST['emp_no']
#         name = request.POST['name']
#         address = request.POST['address']
#         emp_start_date = request.POST['emp_start_date']
#         emp_end_date = request.POST['emp_end_date']
#         status = request.POST['status']

#         if len(request.FILES) !=0:
#             image = request.FILES['image']

#         mydata.Emp_no=emp_no
#         mydata.Name=name
#         mydata.Address=address
#         mydata.Emp_start_date=emp_start_date
#         mydata.Emp_end_date=emp_end_date
#         mydata.Image=image
#         mydata.Status=status
#         mydata.save()
#         return redirect('view_details')

#     return render(request,'update.html',{'data':mydata})





