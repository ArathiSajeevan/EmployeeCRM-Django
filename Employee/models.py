from django.db import models

# Create your models here.

class Datas(models.Model):
    Emp_no = models.IntegerField(default="")
    Name = models.CharField(max_length=20,default="")
    Address = models.CharField(max_length=50,default="")
    Emp_start_date = models.DateField(max_length=20,default="")
    Emp_end_date = models.DateField(max_length=20,default="")
    Status= models.CharField(max_length=20,default="")
    
