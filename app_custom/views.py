from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_kpi.forms import *
from app_team.models import *
from app_stock.models import *
from app_sale.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def index (request):
    
    thaiban = Customer_Interest.objects.all()
    if request.method == "POST":
        form = ThaibanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/thaiban")
    else:
        form = ThaibanForm()
   
    context = {

        "form": form,
		"thaiban":thaiban,

    }
    return render (request,'html_customer/customer.html',context)  



@login_required(login_url="/")
def Add_custom (request):
    return render (request,'html_customer/add_customer.html')

@login_required(login_url="/")
def Add_thaiban (request):
    
    thaiban = Customer_Interest.objects.all()
    if request.method == "POST":
        form = ThaibanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/thaiban")
    else:
        form = ThaibanForm()
     
    context = {

        "form": form,
		"thaiban":thaiban,

    }
    
    return render (request,'html_customer/add_thaiban.html',context)


@login_required(login_url="/")
def Add_duckbet (request):
    
    return render (request,'html_customer/add_duckbet.html')

@login_required(login_url="/")
def Add_rx7 (request):
    
    return render (request,'html_customer/add_rx7.html')

@login_required(login_url="/")
def Add_football (request):
    
    
    
    return render (request,'html_customer/add_football.html')

@login_required(login_url="/")
def Add_huay (request):
    
    return render (request,'html_customer/add_huay.html')

@login_required(login_url="/")
def Add_muay (request):
    
    return render (request,'html_customer/add_muay.html')

@login_required(login_url="/")
def Add_casino (request):
    
    return render (request,'html_customer/add_casino.html')

@login_required(login_url="/")
def Add_lulet (request):
    
    return render (request,'html_customer/add_lulet.html')

@login_required(login_url="/")
def Add_bacara (request):
    
    return render (request,'html_customer/add_bacara.html')
@login_required(login_url="/")
def Add_game (request):
    
    return render (request,'html_customer/add_game.html')

@login_required(login_url="/")
def Edit_custom (request):
    return render (request,'html_customer/edit_customer.html')



@login_required(login_url="/")
def Update_custom (request,pk):
    
    customer = Sale.objects.filter(pk=pk)
    
    context = {
        'customer':customer,
    }
    return render (request,'html_customer/edit_customer.html',context)
@login_required(login_url="/")
def Delete_custom (request):
    return render (request,'html_customer/delete_customer.html')

@login_required(login_url="/")
def Search_custom (request):
    return render (request,'html_customer/delete_customer.html')


@login_required(login_url="/")
def Report_custom (request):
    return render (request,'html_customer/report_customer.html')


@login_required(login_url="/")
def Profile_customer (request,pk):
    
    profile_custermer = Sale.objects.filter(pk=pk)
    
    print("CURRENT :",profile_custermer)
    
    context = {

		"profile_custermer": profile_custermer,



	}

    return render (request,'html_customer/profile_customer.html',context)