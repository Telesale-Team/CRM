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
	path('at/',At,name='at'),
	path('mt/',Mt,name='mt'),
	path('st/',St,name='st'),
	path('ad/',Ad,name='ad'),
	path('it/',It,name='it'),
	

]