from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForms (UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields =["username","email","password1","password2","is_active"]
        
class ProfileForm(forms.ModelForm):

    class Meta:

        model = ProfileUser
        fields = '__all__'
        
class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill
        fields = '__all__'
        
class TeamForm(forms.ModelForm):

    class Meta:

        model = Team
        fields = '__all__'
        
class PositionForm(forms.ModelForm):

    class Meta:

        model = Positions
        fields = '__all__'
        
