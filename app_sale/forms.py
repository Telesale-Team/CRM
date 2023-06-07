from django import forms
from app_sale.models import *
from django.core.validators import RegexValidator

class SaleForm(forms.ModelForm):

    
    class Meta:

        model = Sale
        fields = '__all__'
        
        
        

