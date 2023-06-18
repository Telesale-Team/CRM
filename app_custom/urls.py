from django.urls import path,include

from .views import *


urlpatterns = [
    path('',index),
    path('add_customer/',Add_custom),
    path('thaiban/',Add_thaiban),
    path('duckbet/',Add_duckbet),
    path('rx7/',Add_rx7),
    path('football/',Add_football),
    path('huay/',Add_huay),
    path('muay/',Add_muay),
    path('casino/',Add_casino),
    path('bacara/',Add_bacara),
    path('game/',Add_game),
    path('lulet/',Add_lulet),
    path('profile_customer/<int:pk>',Profile_customer,name='profile-customer'),
    path('update_customer/<int:pk>',Update_custom,name='update-customer'),
    path('delete_customer/',Delete_custom,name='delete-customer'),
    path('edit_customer/',Edit_custom,name='edit-customer'),
    path('report_customer/',Report_custom),
    
   
]