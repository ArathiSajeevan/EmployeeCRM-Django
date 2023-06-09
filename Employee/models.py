import datetime
import os
from django.db import models

def filepath(request,filename):
    old_filenmame = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filenmame) 
    return os.path.join('uploads/', filename)
# Create your models here.

# class Datas(models.Model):
#     Emp_no = models.IntegerField(default="")
#     Name = models.CharField(max_length=20,default="")
#     Address = models.CharField(max_length=50,default="")
#     Emp_start_date = models.DateField(max_length=20,default="", blank=True)
#     Emp_end_date = models.DateField(max_length=20,default="")
#     Image = models.ImageField(upload_to=filepath,null=True, blank=True)
#     Status= models.CharField(max_length=20,default="")

class EmployeeDatas(models.Model):
    emp_no = models.CharField(max_length=20,default="")
    name = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=50,default="")
    emp_start_date = models.CharField(max_length=20,default="", blank=True)
    emp_end_date = models.CharField(max_length=20,default="")
    image = models.ImageField(upload_to=filepath)
    status= models.CharField(max_length=20,default="")



   