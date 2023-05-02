from django.urls import path
from .views import *

urlpatterns = [
    #employee controls
    path('home',home,name="home"),
    path('addData',addData,name="addData"),
    path('updateData/<int:id>',updateData,name="updateData"),
    path('deleteData/<int:id>',deleteData,name="deleteData"),

]
