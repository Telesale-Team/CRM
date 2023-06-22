from django import forms
from app_sale.models import *
from django.core.validators import RegexValidator

class SaleForm(forms.ModelForm):
    other = forms.CharField(
        label='หมายเหตุ',min_length=3, max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'บันทึกข้อมูลเพิ่มเติม '}))
    
    class Meta:

        model = Sale
        fields = '__all__'
        
        
        

