from django import forms
from .models import *
from django.core.validators import RegexValidator

class StockForm(forms.ModelForm):
    
    name = forms.CharField(
        label='ชื่อสินค้า',min_length=3, max_length=50,required=True,
        widget=forms.TextInput(attrs={'placeholder':'ชื่อสินค้า'}))
    
    serial = forms.CharField(
        label='รหัสสินค้า',min_length=3, max_length=50,required=True,
        widget=forms.TextInput(attrs={'placeholder':'รหัสสินค้า'}))
    
    
    detail = forms.CharField(
        label='หมายเหตุ',min_length=3, max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'บันทึกข้อมูลเพิ่มเติม '}))
    
    quatity = forms.CharField(
        label='จำนวนสินค้า',min_length=1, max_length=3,required=True,
        widget=forms.TextInput(attrs={'placeholder':'จำนวนสินค้า'}))
    
    class Meta:

        model = Stock
        fields = '__all__'
        
        
        















class Update_Stock_Form(forms.ModelForm):

    class Meta:

        model = Stock
        fields = '__all__'
        


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'
        
        

        