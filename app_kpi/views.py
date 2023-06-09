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

    Rank_Quatity_data = Sale.objects.all().order_by('-quantity')[:3]
    all_customer = Sale.objects.all()

    #RX7 Data
    rx7 = all_customer.filter(web=1).count()  
    rx7_ads = all_customer.filter(source=1,web=1).count()
    rx7_seo = all_customer.filter(source=2,web=1).count()
    rx7_live = all_customer.filter(source=3,web=1).count()  
    rx7_buy = all_customer.filter(web=1,buy='ซื้อ').count()
    rx7_nobuy = all_customer.filter(web=1,buy='ยังไม่ซื้อ').count()

    #Thaibaan Data
    Thaibaan = all_customer.filter(web=2).count()  
    Thaibaan_ads = all_customer.filter(source=1,web=2).count()
    Thaibaan_seo = all_customer.filter(source=2,web=2).count()
    Thaibaan_live = all_customer.filter(source=3,web=2).count()  
    Thaibaan_buy = all_customer.filter(web=2,buy='ซื้อ').count()
    Thaibaan_nobuy = all_customer.filter(web=2,buy='ยังไม่ซื้อ').count()

    #Duckbet Data
    Duckbet = all_customer.filter(web=3).count()  
    Duckbet_ads = all_customer.filter(source=1,web=3).count()
    Duckbet_seo = all_customer.filter(source=2,web=3).count()
    Duckbet_live = all_customer.filter(source=3,web=3).count()  
    Duckbet_buy = all_customer.filter(web=3,buy='ซื้อ').count()
    Duckbet_nobuy = all_customer.filter(web=3,buy='ยังไม่ซื้อ').count()
    
    #Mughuay Data
    Mughuay = all_customer.filter(web=4).count()  
    Mughuay_ads = all_customer.filter(source=1,web=4).count()
    Mughuay_seo = all_customer.filter(source=2,web=4).count()
    Mughuay_live = all_customer.filter(source=3,web=4).count()  
    Mughuay_buy = all_customer.filter(web=4,buy='ซื้อ').count()
    Mughuay_nobuy = all_customer.filter(web=4,buy='ยังไม่ซื้อ').count()
    
    #Total
    ads = all_customer.filter(source=1)
    seo = all_customer.filter(source=2)

    live = all_customer.filter(source=3)
    
    #สื่อทำการตลาด
    web = Web.objects.all()[:3]
    interest = Interest.objects.all()[:3]
    source = Source.objects.all()[:3]
    
    
    all_register = all_customer
    customer_register_buy = all_customer.filter(buy="ซื้อ")
    customer_register_nobuy = all_customer.filter(buy="ยังไม่ซื้อ")
    

    
    context = {
        
        # source = Live(3) SEO(2) ADS(1)
        # Web = Mughuay(4) Duckbet(3) Thaibaan(2) 7RX7(1)
        
        "all_customer":all_customer,
        "web":web,
        "interest":interest,
        "source":source,
        
        #rx7
        
        "rx7":rx7,
        "rx7_ads":rx7_ads,
        "rx7_seo":rx7_seo,
        "rx7_live":rx7_live,
        "rx7_buy":rx7_buy,
        "rx7_nobuy":rx7_nobuy,
        
        #Thaibaan
        "Thaibaan":Thaibaan,
        "Thaibaan_ads":Thaibaan_ads,
        "Thaibaan_seo":Thaibaan_seo,
        "Thaibaan_live":Thaibaan_live,
        "Thaibaan_buy":Thaibaan_buy,
        "Thaibaan_nobuy":Thaibaan_nobuy,
        
        #Duckbet
        "Duckbet":Duckbet,
        "Duckbet_ads":Duckbet_ads,
        "Duckbet_seo":Duckbet_seo,
        "Duckbet_live":Duckbet_live,
        "Duckbet_buy":Duckbet_buy,
        "Duckbet_nobuy":Duckbet_nobuy,
        
        #Mughuay
        "Mughuay":Mughuay,
        "Mughuay_ads":Mughuay_ads,
        "Mughuay_seo":Mughuay_seo,
        "Mughuay_live":Mughuay_live,
        "Mughuay_buy":Mughuay_buy,
        "Mughuay_nobuy":Mughuay_nobuy,
        
        #Total
        "ads":ads,
        "seo":seo,
        "live":live,
        "all_register":all_register,
        "customer_register_buy":customer_register_buy,
        "customer_register_nobuy":customer_register_nobuy,
        "Rank_Quatity_data":Rank_Quatity_data,
        
        
        #Dashboard
        "count_all":all_customer,
		"count_thaibarn":Sale.objects.all().filter(interest=1).count(),
		"count_huay_online":Sale.objects.all().filter(interest=2).count(),
		"count_huay_football":Sale.objects.all().filter(interest=6).count(),
		"count_huay_casino":Sale.objects.all().filter(interest=5).count(),
  		"count_huay_bacara":Sale.objects.all().filter(interest=4).count(),
		"count_huay_slot":Sale.objects.all().filter(interest=3).count(),
		"buy":Sale.objects.all().filter(buy="ซื้อ").count(),
  		"nobuy":Sale.objects.all().filter(buy="ยังไม่ซื้อ").count(),
        "total":Sale.objects.all().filter(buy="ซื้อ").order_by('-quantity')[:3]
        


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



