
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app_user.models import ProfileUser
from .forms import *
from app_user.filters import UserFilter
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def register(request):
	
	users = ProfileUser.objects.all()

	
	user_filter = UserFilter(request.GET,queryset=User.objects.all())
	filter_user = user_filter.form
	user_data = user_filter.qs
 
	page = Paginator(user_data,10)
	page_list = request.GET.get("page")
	page_data = page.get_page(page_list)

	if request.method == 'POST':
		form_user = RegistrationForm(request.POST)
		
		if form_user.is_valid():
			username = form_user.save()
			ProfileUser.objects.create(username=username)
			return redirect('user-search')  # Redirect to user profile page
	else:
		form_user = RegistrationForm()
	
	
	
	context = {
		"users":users,
		"form_user":form_user,
		"filter_user":filter_user,
		"page_data":page_data,
	}
	return render(request, 'html_login/register.html', context)



@login_required(login_url="/")
def Search_user (request):

	user_filter = UserFilter(request.GET,queryset=User.objects.all())
	filter_user = user_filter.form
	user_data = user_filter.qs
 
	page = Paginator(user_data,10)
	page_list = request.GET.get("page")
	page_data = page.get_page(page_list)
 
 
	context = {


		"filter_user":filter_user,
		"page_data":page_data,
	}
	
	return render(request,'html_user/search_user.html',context)