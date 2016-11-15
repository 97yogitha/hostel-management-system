from .models import Student,MessMenu, Hostel_office , Mess , Complaint
from django.contrib.auth.models import User
from django import forms
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ('sem','dob','roll_no','reg_no','hostel_feeno','coll_feeno','mess_no','branch','mess_names','hostel_block','room_no')

class AdminForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = Hostel_office
		fields = ('dept_no',)
class MessForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = Mess
		fields = ('per_day_cost','mess_name')

class ComplaintForm(forms.ModelForm):
	class Meta:
		model = Complaint
		fields = ('c_category','c_description','c_deptno')

class MenuForm(forms.ModelForm):
	class Meta:
		model = MessMenu
		fields = ('day','morning','afternoon','snacks','dinner')
'''class StudentUpdate(UpdateView):
	model = Student
	fields = ['sem','mess_names','hostel_block','room_no']'''

class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('sem', 'branch', 'mess_names', 'hostel_block')