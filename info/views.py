from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import UserForm,ComplaintForm, StudentForm, MessForm,AdminForm,MenuForm, UpdateProfileForm
from django.template import RequestContext
from .models import Student, Hostel_office , Mess, Room, Complaint,  Hostel_block , MessMenu
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.utils import timezone
from django.db import models
from django.http import StreamingHttpResponse
from django.views.generic import View
from info.models import Mess
import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str

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
		return render(request,'info/login.html')

	else:
		context = {
	        'user_form':user_form,
	        'profile_form':profile_form,
	    }
		return render(request,'info/register.html',context)

def updateprofile_new(request):
	form = UpdateProfileForm(request.POST or None)
	student = Student.objects.get(user = request.user)
	if form.is_valid() and request.method== "POST":
		
		sem = request.POST["sem"]
		hostel = request.POST["hostel_block"]
		hostel_inst = Hostel_block.objects.get(block_no=hostel)
		branch = request.POST["branch"]
		mess_names = request.POST["mess_names"]
		mess_name = Mess.objects.get(mess_name=mess_names)
		
		student.sem = sem
		student.hostel_block = hostel_inst
		student.branch = branch

		student.mess_names = mess_name
		student.save()
		student = Student.objects.get(user=request.user)
		room = Room.objects.get(room_no = str(student.room_no))
		hostel = Hostel_block.objects.get(block_no = str(room.block_no))

		mess = Mess.objects.get(mess_name = student.mess_names)
		
		context = {
			'student':student,
			'room':room,
			'hostel':hostel,
			'mess':mess,
			'roll_no': student.roll_no,
		
		}
		return render(request,'info/index.html',context)
	else:
		context = {
					'form' : form,
		}
		return render(request,'info/update_profile.html',context)

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username = username,password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				student = Student.objects.get(user=request.user)
				room = Room.objects.get(room_no = str(student.room_no))
				hostel = Hostel_block.objects.get(block_no = str(room.block_no))

				mess = Mess.objects.get(mess_name = student.mess_names)
		
				context = {
					'student':student,
					'room':room,
					'hostel':hostel,
					'mess':mess,
					'roll_no': student.roll_no,
		
				}
				return render(request,'info/index.html',context)
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

def login_admin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate (username = username,password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				hosteloffice = Hostel_office.objects.get(huser= request.user)
				complaints = Complaint.objects.all()
				hostel = Hostel_block.objects.all()
				hostelblock = hostel.count()
				h= Hostel_block.objects.get(block_no=2)
				room = Room.objects.all()
				block2=h.room_set.count()
				h= Hostel_block.objects.get(block_no=1)
				room = Room.objects.all()
				block1=h.room_set.count()
				r1 = Complaint.objects.filter(c_status='Received')
				r = r1.count()
				i1 = Complaint.objects.filter(c_status='In Progress ')
				i = i1.count()
				c1 = Complaint.objects.filter(c_status='Completed ')
				c = c1.count()
				context = {
					'hosteloffice':hosteloffice,
					'r' : r,
					'i' : i,
					'c':c,
					'hostelblock':hostelblock,
					'block1':block1,
					'block2':block2,	
				}
				return render(request,'info/index_admin.html',context)
			else:
				return render(request,'info/login_admin.html',{'error_message':'Your account has been disabled'})

		else:
			return render(request,'info/login_admin.html',{'error_message':'Invalid login'})
	return render(request,'info/login_admin.html')
def admin_profile(request):
	if not request.user.is_authenticated():
		return render(request,'info/login_admin.html')
	else:
		hosteloffice= Hostel_office.objects.get(huser = request.user)
		complaints = Complaint.objects.all()
		hostel = Hostel_block.objects.all()
		hostelblock = hostel.count()
		h= Hostel_block.objects.get(block_no=2)
		room = Room.objects.all()
		block2=h.room_set.count()
		h= Hostel_block.objects.get(block_no=1)
		room = Room.objects.all()
		r1 = Complaint.objects.filter(c_status='Received')
		r = r1.count()
		i1 = Complaint.objects.filter(c_status='In Progress')
		i = i1.count()
		c1 = Complaint.objects.filter(c_status='Completed')
		c = c1.count()
		room = Room.objects.all()
		block1=h.room_set.count()
		context = {
			'hosteloffice':hosteloffice,
			'r' : r,
			'i' : i,
			'c':c,
			'hostelblock':hostelblock,
			'block1':block1,
			'block2':block2,	
		}
		return render(request,'info/index_admin.html',context)

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
				mess = Mess.objects.get(muser = request.user)
				student = Student.objects.all()
				numstu = mess.student_set.count()
				revmonth = numstu*30*mess.per_day_cost
				context ={
					'mess':mess,
					'numstu':numstu,
					'revmonth':revmonth,
				}
				return render(request,'info/index_mess.html',context)
			else:
				return render(request,'info/login_mess.html',{'error_message':'Your account has been disabled'})

		else:
			return render(request,'info/login_mess.html',{'error_message':'Invalid login'})
	return render(request,'info/login_mess.html')
def mess_profile(request):
	if not request.user.is_authenticated():
		return render(request,'info/login_mess.html')
	else:
		mess= Mess.objects.get(muser = request.user)
		student = Student.objects.all()
		numstu = mess.student_set.count()
		revmonth = numstu*30*mess.per_day_cost
		context = {
			'mess':mess,
			'numstu':numstu,
			'revmonth':revmonth,
		}
		return render(request,'info/index_mess.html',context)
def logout_mess(request):
    logout(request)
    form = MessForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'info/login_mess.html', context)

def index(request):
	if not request.user.is_authenticated():
		return render(request,'info/intro.html')
	elif Student.objects.filter(user = request.user).exists():
		student = Student.objects.get(user = request.user)
		complaint = Complaint.objects.filter(user = request.user)
		return render(request,'info/index.html',{'student':student})
	elif Hostel_office.objects.filter(huser = request.user).exists():
		hosteloffice = Hostel_office.objects.get(huser=request.user)
		return render(request,'info/index_admin.html',{'hosteloffice':hosteloffice})
	else:
		mess = Mess.objects.get(muser = request.user)
		return render(request,'info/index_mess.html',{'mess':mess})

def complaint_register(request):
	form = ComplaintForm(request.POST or None)
	if form.is_valid():
		complaint = form.save(commit = False)
		student = Student.objects.get(user = request.user)
		complaint.user = student
		complaint.save()
		return render(request,'info/complaintview.html',{'student':student})
	else:
		context = {
			'form':form,
		}
		return render(request,'info/complaintregister.html',context)
#student viewin his complaints
def complaint_view(request):
	 if not request.user.is_authenticated():
	 	return render(request, 'info/login.html')
	 else:
	 	student = Student.objects.get(user = request.user)
	 	complaints = Complaint.objects.all()
	 	return render(request, 'info/complaintview.html', {'student': student})

def student_menu_view(request):
	if not request.user.is_authenticated():
		return render(request,'info/login.html')
	else:
		student = Student.objects.get(user = request.user)
		messmenu = MessMenu.objects.filter(mess_name=student.mess_names)
		return render(request,'info/studentmessmenu.html',{'messmenu':messmenu})

def complaint_admin(request):
	 if not request.user.is_authenticated():
	 	return render(request, 'info/login_admin.html')
	 else:
	 	complaints = Complaint.objects.all().update(c_status='Received')
	 	complaints = Complaint.objects.order_by('-id')[0:]
	 	return render(request,'info/complaintadmin.html',{'complaints':complaints})

def menu_update(request) :
	form = MenuForm(request.POST or None)
	if form.is_valid():
		menu = form.save(commit=False)
		mess = Mess.objects.get(muser = request.user)
		menu.mess_name = mess
		menu.save()
		menudeleted = MessMenu.objects.filter( day__lt = timezone.now())
		for m in menudeleted:
			m.delete()
		menu = MessMenu.objects.all()
		return render(request,'info/messmenuview.html',{'mess':mess})
	else:
		return render(request,'info/menuupdate.html',{'form':form})

def menu_view(request):
	if not request.user.is_authenticated():
		return render(request,'info/login_mess.html')
	else:
		mess = Mess.objects.get(muser = request.user)
		menudeleted = MessMenu.objects.filter( day__lt = timezone.now())
		for m in menudeleted:
			m.delete()
		menu = MessMenu.objects.all()
		
		return render(request,'info/messmenuview.html',{'mess':mess})

def student_profile(request):
	if not request.user.is_authenticated():
		return render(request,'info/login.html')
	else:
		student= Student.objects.get(user = request.user)
		room = Room.objects.get(room_no = str(student.room_no))
		hostel = Hostel_block.objects.get(block_no = str(room.block_no))
		mess = Mess.objects.get(mess_name = student.mess_names)
		
		context = {
			'student':student,
			'room':room,
			'hostel':hostel,
			'mess':mess,
			
		}
		return render(request,'info/index.html',context)
	#need to add account successfully created
'''def update_profile(request,pk = None):
	instance = get_object_or_404(Student , pk = pk)
	form = UpdateProfileForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
	context ={
		'instance':instance,
		'form':form,

	}
	return render(request,'info/')'''
'''def update_profile(request):
	form = UpdateProfileForm(request.POST or None)
	student = Student.objects.get(user = request.user)
	context = {
			'student':student,
			'form':form,
		}
	if form.is_valid():
		form.save()
		return render(request,'info/index.html',context)
	else:
		return render(request,'info/update_profile.html',context)'''
'''def update_profile(request,num=0):
	form = UpdateProfileForm(request.POST or None)
	if num!=0:
		instance = get_object_or_404(Student, id = num)
		
    	if form.is_valid():
        	form.save()
        	return render(request, 'info/index.html',{'form':form,'student':student})
	else:
		user = request.user
    	student = Student.objects.get(user=user)
    	return render(request, 'info/update_profile.html', {'form':form,'student':student})
    
'''

def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Mess, 'xls', file_name="sheet")
    elif atype == "mess":
        return excel.make_response_from_tables(
            [Mess, User], 'xls', file_name="Mess")