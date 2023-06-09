from django import forms
from Employee.models import EmployeeDatas

class RegisterForm(forms.Form):
    emp_no = forms.CharField(label="Employee Number", max_length=100)
    name = forms.CharField(label="Employee Name", max_length=100)
    address = forms.CharField(label="Employee Address", max_length=100)
    emp_start_date = forms.CharField(label="Start Date", max_length=100)
    emp_end_date = forms.CharField(label="End Date", max_length=100)
    image = forms.ImageField(label="Employee Image", max_length=100)
    status = forms.CharField(label="Employee Status", max_length=100)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeDatas
        fields = ['emp_no','name','address','emp_start_date','emp_end_date','status']

    emp_no = forms.CharField(label="Employee Number", max_length=100)
    name = forms.CharField(label="Employee Name", max_length=100)
    address = forms.CharField(label="Employee Address", max_length=100)
    emp_start_date = forms.CharField(label="Start Date", max_length=100)
    emp_end_date = forms.CharField(label="End Date", max_length=100)
    # image = forms.ImageField()
    status = forms.CharField(label="Employee Status", max_length=100)
