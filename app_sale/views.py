from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app_sale.forms import *
from app_sale.filters import *
from app_sale.models import *
from django.core.paginator import Paginator


# Create your views here.

@login_required(login_url="/")
def Index (request):
	sale = Sale.objects.all()
	count_all=sale.count()
	
	
	#Form
	if request.method == "POST":
		form_sale = SaleForm(request.POST)
		if form_sale.is_valid():
			form_sale.save()
			return redirect("sale-home")
	else:
		form_sale = SaleForm()	
	
	#Filter
	filter = SaleFilter(request.GET,queryset=Sale.objects.all())
	filter_sale = filter.form
	query_sale = filter.qs
	
 
	#Paginator
	page = Paginator(query_sale,20)
	page_list = request.GET.get("page")
	page_sale = page.get_page(page_list)
	context = {

		"form_sale":form_sale,
		"filter_sale":filter_sale,
		"page_sale":page_sale,
		"count_all":count_all,
		"count_thaibarn":Sale.objects.all().filter(interest=1).count(),
		"count_huay_online":Sale.objects.all().filter(interest=2).count(),
		"count_huay_football":Sale.objects.all().filter(interest=6).count(),
		"count_huay_casino":Sale.objects.all().filter(interest=5).count(),
  		"count_huay_bacara":Sale.objects.all().filter(interest=4).count(),
		"count_huay_slot":Sale.objects.all().filter(interest=3).count(),
		"buy":Sale.objects.all().filter(buy="ซื้อ").count(),
  		"nobuy":Sale.objects.all().filter(buy="ยังไม่ซื้อ").count(),
	}
  
  
	return render(request,'html_sale/sale.html',context)


@login_required(login_url="/")
def Update_Sale (request,pk ):
	

	customer = get_object_or_404(Sale, pk=pk)

	if request.method == "POST":
		form_update_sale = SaleForm(request.POST,request.FILES,instance=customer)
		if form_update_sale.is_valid():
			form_update_sale.save()
			return redirect("sale-home")
	else:
		form_update_sale = SaleForm(instance=customer)
		
		
	context = {

		"form_update_sale": form_update_sale,
		"customer":customer,
	}

	return render (request,'html_sale/update_sale.html',context)


@login_required
def Delete_Sale(request,pk):
	
	customer = Sale.objects.get(pk=pk)
	
	if request.method == 'POST':
		customer.delete()
		return redirect('sale-home')  # Redirect to home page or any other appropriate page
	else:
		return render(request, 'html_sale/delete_sale.html', {'customer': customer})