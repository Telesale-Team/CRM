
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app_user.models import ProfileUser


class RegistrationForm (UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User
        fields =["username","first_name","email","last_name","password1","password2"]
        labels = {
            'username':'รหัสพนักงาน',
            'Email':'อีเมลล์',
            'first_name':'ชื่อจริง',
            'last_name':'นามสกุล',
            'password1':'พาสเวิร์ด',
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'รหัสพนักงาน เช่น 1001'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'เช่น กิ่งแก้ว'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'เช่น ปานจะงาม'}),
        }