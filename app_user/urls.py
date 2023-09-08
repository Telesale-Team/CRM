from django.urls import path,include
from app_user.views import *
from app_login.views import Search_user

urlpatterns = [
    
	path('',Dashboard,name="home-user"),
 
	path('position/<str:position>',PositionGroup,name='search-position'),
   	path('report_user/',Report_user),

	path('add_team/',Add_Team,name='add-team'),
 	path('update_team/<int:pk>',Update_Team,name='update-team'),
  	path('delete_team/<int:pk>',Delete_Team,name='delete-team'),

	path('add_skill/',Add_Skill,name='add-skill'),
 	path('update_skill/<int:pk>',Update_Skill,name='update-skill'),
  	path('delete_skill<int:pk>',Delete_Skill,name='delete-skill'),

	path('profile/update/<int:pk>/',Update_profile,name='profile-update'),
	path('profile/delete/<int:pk>/',Delete_profile, name='profile-delete'),
	
	path('add_position/',Add_Position,name='add-position'),
 	path('position/update/<int:id>/',Update_Position,name='position-update'),
	path('position/delete/<int:id>/',Delete_Position,name='position-delete'),
	
	path('edit/<int:pk>/',Edit_user,name='user-edit'),
	path('update/<int:pk>/',Update_user,name='user-update'),
	path('delete/<int:pk>/',Delete_user, name='user-delete'),
 	path('Search/<int:pk>/',Search_user, name='user-search'),
 
 	path('hr/',Hr,name='hr'),
	path('hunter/',Hunter,name='hunter'),
	path('telesale/',Telesale,name='telesale'),
	path('entertenment/',Entertenment,name='entertenment'),
	path('ad/',Ad,name='ad'),
	path('stock-data/',Data_Stock,name='stock-data'),
 	path('money-data/',Data_Money,name='money-data'),
	path('seo-data/',Data_Seo,name='seo-data'),
 	path('live-data/',Data_live,name='live-data'),
	path('graphic-data/',Data_Graphic,name='graphic-data'),
	path('admin-data/',Data_admin,name='admin-data'),
	
]