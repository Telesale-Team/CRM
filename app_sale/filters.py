import django_filters
from .models import *

class SaleFilter(django_filters.FilterSet):

    class Meta:
        model = Sale
        fields = {

            "user_account":['exact'],
            "name":['icontains'],
            "interest":['exact'],
            "source":['exact'],
            "web":['exact'],
            "sex":['exact'],
            "buy":['exact'],
    }