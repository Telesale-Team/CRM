import django_filters
from app_user.models import *

class ProfileFilter(django_filters.FilterSet):

	class Meta:
		model = ProfileUser
		fields = {
					'username':['exact'],
					'nickname':['icontains'],
					'team':['exact'],
					'position':['exact'],
					
				  }

  
  
class UserFilter(django_filters.FilterSet):

	class Meta:
		model = User
		fields = {
            'username':['icontains'],
            
            }
    
class PositionFilter(django_filters.FilterSet):

	class Meta:
		model = Positions
		fields = {
				  'name':['icontains'],
				  }


class TeamFilter(django_filters.FilterSet):

	class Meta:
		model = Team
		fields = {
				  'name':['icontains'],
				  }
		
class SkillFilter(django_filters.FilterSet):

	class Meta:
		model = Skill
		fields = {
				  'name':['icontains'],
				  }