from django.urls import path,include
from app_user.views import *
from .views import *
urlpatterns = [
	path('',Index,name="sale-home"),
    path('update/<int:pk>',Update_Sale,name="update-sale"),
    path('delete/<int:pk>',Delete_Sale,name="delete-sale"),
 
	

]