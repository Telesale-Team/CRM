from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_kpi.models import *
from app_team.models import *
from app_stock.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import *
from app_sale.models import *
from app_user.models import ProfileUser

# Create your views here.
@login_required(login_url="/")
def Dashboards (request):

    # 10Rank user

    data = Sale.objects.all().order_by('-quantity')[:10]



    sale_user = Sale.objects.all().order_by('-quantity')


    context = {
        # source = Live(3) SEO(2) ADS(1)
        # Web = Mughuay(4) Duckbet(3) Thaibaan(2) 7RX7(1)
        

        ######## SEO ########

        #SEO 7RX7
        "seo_rx" : Sale.objects.all().filter(source=2,web=1).count(), 
        "seo_rx_buy" : Sale.objects.all().filter(source=2,web=1,buy="ซื้อ").count(),
        "seo_rx_nobuy" : Sale.objects.all().filter(source=2,web=1,buy="ยังไม่ซื้อ").count(),
        
        # SEO Duckbet
        "seo_duckbet" : Sale.objects.all().filter(source=2,web=3).count(),
        "seo_duckbet_buy" : Sale.objects.all().filter(source=2,web=3,buy="ซื้อ").count(),
        "seo_duckbet_nobuy" : Sale.objects.all().filter(source=2,web=3,buy="ยังไม่ซื้อ").count(),
        
        # SEO Thaibaan
        "seo_thaibaan_all" : Sale.objects.all().filter(source=2,web=2).count(),
        "seo_thaibaan_buy" : Sale.objects.all().filter(source=2,web=2,buy="ซื้อ").count(),
        "seo_thaibaan_nobuy" : Sale.objects.all().filter(source=2,web=2,buy="ยังไม่ซื้อ").count(),
        
        # SEO Munghuay
        "seo_mughuay_all" : Sale.objects.all().filter(source=2,web=4).count(),
        "seo_mughuay_buy" : Sale.objects.all().filter(source=2,web=4,buy="ซื้อ").count(),
        "seo_mughuay_nobuy" : Sale.objects.all().filter(source=2,web=4,buy="ยังไม่ซื้อ").count(),


        "Total seo_buy" :
        Sale.objects.all().filter(source=2,web=1,buy="ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=2,buy="ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=3,buy="ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=4,buy="ซื้อ").count(),

        "Total seo_nobuy" : 
        Sale.objects.all().filter(source=2,web=1,buy="ยังไม่ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=2,buy="ยังไม่ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=3,buy="ยังไม่ซื้อ").count()+
        Sale.objects.all().filter(source=2,web=4,buy="ยังไม่ซื้อ").count(),

        # SEO Buy All Product
        "seo_all_product" : 
        Sale.objects.all().filter(source=2,web=1).count()+ 
        Sale.objects.all().filter(source=2,web=3).count()+
        Sale.objects.all().filter(source=2,web=2).count()+
        Sale.objects.all().filter(source=2,web=4).count(),



        ######## 7RX7 ########

        #ADS 7RX7
        "ADS_rx" : Sale.objects.all().filter(source=1,web=1).count(), 
        "ADS_rx_buy" : Sale.objects.all().filter(source=1,web=1,buy="ซื้อ").count(),
        "ADS_rx_nobuy" : Sale.objects.all().filter(source=1,web=1,buy="ยังไม่ซื้อ").count(),
        
        # ADS Thaibaan
        "ADS_thaibaan_all" : Sale.objects.all().filter(source=1,web=2).count(),
        "ADS_thaibaan_buy" : Sale.objects.all().filter(source=1,web=2,buy="ซื้อ").count(),
        "ADS_thaibaan_nobuy" : Sale.objects.all().filter(source=1,web=2,buy="ยังไม่ซื้อ").count(),

        # ADS Duckbet
        "ADS_duckbet" : Sale.objects.all().filter(source=1,web=3).count(),
        "ADS_duckbet_buy" : Sale.objects.all().filter(source=1,web=3,buy="ซื้อ").count(),
        "ADS_duckbet_nobuy" : Sale.objects.all().filter(source=1,web=3,buy="ยังไม่ซื้อ").count(),
        
        # ADS Munghuay
        "ADS_mughuay_all" : Sale.objects.all().filter(source=1,web=4).count(),
        "ADS_mughuay_buy" : Sale.objects.all().filter(source=1,web=4,buy="ซื้อ").count(),
        "ADS_mughuay_nobuy" : Sale.objects.all().filter(source=1,web=4,buy="ยังไม่ซื้อ").count(),

        #ADS Buy



        #Live 7RX7
        "live_rx" : Sale.objects.all().filter(source=1,web=1).count(), 
        "live_rx_buy" : Sale.objects.all().filter(source=1,web=1,buy="ซื้อ").count(),
        "live_rx_nobuy" : Sale.objects.all().filter(source=1,web=1,buy="ยังไม่ซื้อ").count(),
        
        # live Thaibaan
        "live_thaibaan_all" : Sale.objects.all().filter(source=1,web=2).count(),
        "live_thaibaan_buy" : Sale.objects.all().filter(source=1,web=2,buy="ซื้อ").count(),
        "live_thaibaan_nobuy" : Sale.objects.all().filter(source=1,web=2,buy="ยังไม่ซื้อ").count(),

        # live Duckbet
        "live_duckbet" : Sale.objects.all().filter(source=1,web=3).count(),
        "live_duckbet_buy" : Sale.objects.all().filter(source=1,web=3,buy="ซื้อ").count(),
        "live_duckbet_nobuy" : Sale.objects.all().filter(source=1,web=3,buy="ยังไม่ซื้อ").count(),
        
        # live Munghuay
        "live_mughuay_all" : Sale.objects.all().filter(source=1,web=4).count(),
        "live_mughuay_buy" : Sale.objects.all().filter(source=1,web=4,buy="ซื้อ").count(),
        "live_mughuay_nobuy" : Sale.objects.all().filter(source=1,web=4,buy="ยังไม่ซื้อ").count(),
        
        

        # source = Live(3) SEO(2) ADS(1)
        # Web = Mughuay(4) Duckbet(3) Thaibaan(2) 7RX7(1)



        # ADS All Product
        "ads_all_product" : 
        Sale.objects.all().filter(source=1,web=1).count()+
        Sale.objects.all().filter(source=1,web=2).count()+
        Sale.objects.all().filter(source=1,web=3).count()+
        Sale.objects.all().filter(source=1,web=4).count(),

        

        #Live All Product
        "live_all_product" :
        Sale.objects.all().filter(source=3,web=1).count()+
        Sale.objects.all().filter(source=3,web=2).count()+
        Sale.objects.all().filter(source=3,web=3).count()+
        Sale.objects.all().filter(source=3,web=4).count(),

        


        "data":data,
        "sale_user":sale_user,




	}
    
    return render (request,'html_kpi/dashboard.html',context)  



@login_required(login_url="/")
def Add_dashboard (request):
	
	if request.method == "POST":
		form = KipForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/user")
	else:
		form = KipForm()
		
	context = {

		"form": form,
        

	}
	 
	return render (request,'html_kpi/add_dashboard.html',context)   

 
 
@login_required(login_url="/")

def Thaibans (request):
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
     
    return render (request,'html_kpi/thaiban.html',context)   