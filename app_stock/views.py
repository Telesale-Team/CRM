from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import *
from .filters import *
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url="/")
def dashboard (request):

	filter_item = StockFilter(request.GET,queryset=Stock.objects.all())
	filter_stock = filter_item.form
	item_stock = filter_item.qs
		
	if request.method == "POST":
		form_stock = StockForm(request.POST)
		if form_stock.is_valid():
			form_stock.save()
			return redirect("/stock")
	else:
		form_stock = StockForm()

	#Paginator
	page = Paginator(item_stock,10)
	page_list = request.GET.get("page")
	page_stock = page.get_page(page_list)
	
	item_count_all = Stock.objects.all().count()
	item_count_computer = Stock.objects.all().filter(category='13').count()
	item_count_cable = Stock.objects.all().filter(category='9').count()
	item_count_office = Stock.objects.all().filter(category='10').count()
	item_count_telephone = Stock.objects.all().filter(category='11').count()
	item_count_notebook = Stock.objects.all().filter(category='8').count()
	context = {

		"form_stock":form_stock,
		"filter_stock":filter_stock,
		"item_stock":item_stock,
		"page_stock":page_stock,
		"item_count_all":item_count_all,
		"item_count_computer":item_count_computer,
		"item_count_cable":item_count_cable,
		"item_count_office":item_count_office,
		"item_count_telephone":item_count_telephone,
		"item_count_notebook":item_count_notebook,

  

	}
	return render(request,'html_stock/stock.html',context)


@login_required(login_url="/")
def Update_Stock (request,pk ):
	

	item = get_object_or_404(Stock, pk=pk)

	if request.method == "POST":
		form_update_stock = Update_Stock_Form(request.POST,request.FILES,instance=item)
		if form_update_stock.is_valid():
			form_update_stock.save()
			return redirect("/stock")
	else:
		form_update_stock = Update_Stock_Form(instance=item)
		
		
	context = {

		"item":item,
		"form_update_stock": form_update_stock,
	}

	return render (request,'html_stock/update_stock.html',context)



@login_required(login_url="/")
def Delete_Stock (request,pk ):
	

	item = get_object_or_404(Stock, pk=pk)

	if request.method == "POST":

		item.delete()
		return redirect("/stock")
	else:
		return render (request,'html_stock/delete_stock.html',{'item':item})



@login_required(login_url="/")
def Add_Category(request):

	items = Category.objects.all()
	if request.method == "POST":
		form = CategoryForm(request.POST )
		if form.is_valid():
			form.save()
			return redirect("/stock")
	else:
		form = CategoryForm()

	context = {
		"items" : items,
		"form" : form,
	}  
   
	return render (request,'html_stock/add_Category.html',context)

