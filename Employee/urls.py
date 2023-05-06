from django.urls import path
from Employee_crm import settings

from Employee_crm.settings import STATIC_URL
from .views import *
from Employee import views

urlpatterns = [
    #employee controls
    path('home',home,name="home"),
    path('addData',addData,name="addData"),
    path('updateData/<int:id>',updateData,name="updateData"),
    path('deleteData/<int:id>',deleteData,name="deleteData"),
    path('view_details',view_details,name="view_details"),

]

# urlpatterns += STATIC_URL(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += STATIC_URL(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)