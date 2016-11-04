from .models import Student, Hostel_office , Mess
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')

class StudentForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = ('sem','dob','roll_no','reg_no','hostel_feeno','coll_feeno','mess_no','branch','mess_names','room_no')
class AdminForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = Hostel_office
		fields = ('dept_no',)

class MessForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())
	class Meta:
		model = Mess
		fields = ('mess_name','per_day_cost','day','morning','afternoon','snacks','dinner')

