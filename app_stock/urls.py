from django.urls import path,include

from .views import *


urlpatterns = [
    path('',dashboard,name='stock'),
    path('add_Category/',Add_Category,name="add_Category"),
    path('update/<int:pk>',Update_Stock,name="update-stock"),
    path('delete/<int:pk>',Delete_Stock,name="delete-stock"),
    path('add_Category/delete/<int:pk>',Delete_Category,name="delete-category"),
    path('add_Category/update/<int:pk>',Update_Category,name="update-category"),
    path('filter/notebook',Filter_Notebook,name="filter-notebook"),
    path('filter/pc',Filter_Pc,name="filter-pc"),
    path('filter/monitor',Filter_Monitor,name="filter-monitor"),
    path('filter/headphone',Filter_Headphone,name="filter-headphone"),
    path('filter/keyboard',Filter_Keyboard,name="filter-keyboard"),
    path('filter/Mount',Filter_Mount,name="filter-Mount"),
    path('filter/Extension',Filter_Extension,name="filter-Extension"),
    path('filter/Office',Filter_Office,name="filter-Office"),
    path('filter/Cable',Filter_Cable,name="filter-Cable"),
    path('filter/Padmount',Filter_Padmount,name="filter-Padmount"),
    path('filter/Phone',Filter_Phone,name="filter-Phone"),
]