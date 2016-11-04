from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import UserForm, StudentForm, AdminForm,MessForm
from django.template import RequestContext
from .models import Student, Hostel_office , Mess, Room, Complaint, Writes, Hostel_block
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def register(request):
	user_form = UserForm(data = request.POST or None)
	profile_form = StudentForm(data = request.POST or None)

	
	if user_form.is_valid() and profile_form.is_valid():
		#save the user information to database
		user = user_form.save()
		user.set_password(user.password)
		user.save()
		
		profile = profile_form.save(commit=False)
		profile.user = user
		profile.save()
	context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
	return render(request,'info/register.html',context)

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username = username,password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				student = Student.objects.get(user=request.user)
				return render(request,'info/index.html',{'student':student})
			else:
				return render(request,'info/login.html',{'error_message':'Your account has been disabled'})

		else:
			return render(request,'info/login.html',{'error_message':'Invalid login'})
	return render(request,'info/login.html')
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'info/login.html', context)

'''def index(request):
    if not request.user.is_authenticated():
    	
        return render(request, 'info/intro.html')
    else:
    	try:
    		student = Student.objects.get(user=request.user)
        	return render(request,'info/index.html',{'student':student})
        except ObjectDoesNotExist:
        	try:
        		hosteloffice = Hostel_office.objects.get(user = request.user)
        		return render(request,'info/index_admin.html',{'hosteloffice':hosteloffice})
        	except:
        		mess = Mess.objects.get(user = request.user)
        		return render(request,'info/index_mess.html',{'mess':mess})'''

def index(request):
	if not request.user.is_authenticated():
		return render(request,'info/intro.html')
	else:
		if Student.objects.get(user=request.user).exists():
			student = Student.objects.get(user=request.user)
			return render(request,'info/index.html',{'student':student})
		elif Hostel_office.objects.get(user = request.user).exists():
			hosteloffice = Hostel_office.objects.get(user = request.user)
        	return render(request,'info/index_admin.html',{'hosteloffice':hosteloffice})





def login_admin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username = username,password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'info/index.html')
			else:
				return render(request,'info/login_admin.html',{'error_message':'Your account has been disabled'})

		else:
			return render(request,'info/login_admin.html',{'error_message':'Invalid login'})
	return render(request,'info/login.html')

def logout_admin(request):
    logout(request)
    form = AdminForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'info/login_admin.html', context)

def login_mess(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username = username,password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'info/index.html')
			else:
				return render(request,'info/login_mess.html',{'error_message':'Your account has been disabled'})

		else:
			return render(request,'info/login_mess.html',{'error_message':'Invalid login'})
	return render(request,'info/login.html')

def logout_mess(request):
    logout(request)
    form = AdminForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'info/login_mess.html', context)