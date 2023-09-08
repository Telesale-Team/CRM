from django.urls import path,include

from .views import *


urlpatterns = [
    path('',Dashboards,name='dashboard' ),
    path('add_dashbaord/',Add_dashboard ),
    path('thaiban/',Thaibans ),
    path('kpi/',KPI,name='kpi'),
    path('check_kpi/<str:name>',Check_Kpi,name='check-kpi'),
    path('update_kpi/<str:name>',Update_Kpi,name='update-kpi'),

]
