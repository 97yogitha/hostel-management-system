from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Hostel_block(models.Model):
		
	ROOM_TYPE = (
		('SSR','single shared room'),
		('DSR','double shared room'),
		('TSR','triple shared room'),
		('D','dormitory'),
		)
	block_no = models.IntegerField(primary_key=True)
	room_type = models.CharField(max_length=20, choices = ROOM_TYPE)
	room_cost = models.IntegerField()

	def __str__(self):
		return str(self.block_no)
	
class Mess(models.Model):
	muser = models.OneToOneField(User,on_delete=models.CASCADE)
	MESS_NAME = (('IH','girls hostel top mess'),
					('GH','girls hostel down mess'),
					('MM','Mega mess'),
					('FB','First Block mess'),
					('SB','Second Block mess'),
					('TB','Third Block mess'),
					)
	mess_name = models.CharField(max_length=25, choices = MESS_NAME,primary_key=True)
	per_day_cost = models.IntegerField()
	def __str__(self):
		return self.mess_name

class MessMenu(models.Model):
	mess_name = models.ForeignKey(Mess,on_delete=models.CASCADE)
	day = models.DateField(default=timezone.now())
	morning = models.TextField()
	afternoon = models.TextField()
	snacks = models.TextField()
	dinner = models.TextField()
	def __str__(self):
		return str(self.day)

class Room(models.Model):

	room_no = models.IntegerField()
	validity = models.DateField()
	block_no = models.ForeignKey(Hostel_block,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.room_no)

class Student(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	sem = models.IntegerField()
	dob = models.DateField()
	roll_no = models.CharField(max_length=6, unique=True,primary_key=True)
	reg_no = models.CharField(max_length=6,unique=True)
	hostel_feeno = models.CharField(max_length=6,unique=True)
	coll_feeno = models.CharField(max_length=6,unique=True,blank=True)
	mess_no = models.IntegerField(blank=True)
	branch = models.CharField(max_length=25)
	hostel_block = models.ForeignKey(Hostel_block)
	room_no = models.OneToOneField(Room)
	mess_names = models.ForeignKey(Mess)

	def __str__(self):
		return self.user.username

class Hostel_office(models.Model):
	huser = models.OneToOneField(User)
	dept_no = models.IntegerField(primary_key=True)

	def  __str__(self):
		return self.huser.username
		
class Complaint(models.Model):
	user = models.ForeignKey(Student)
	STATUS = (	('Sent','Sent'),
				('Received','Received'),
				('In Progress','In Progress'),
				('Completed','Completed'),
				)
	c_category = models.CharField('Category',max_length=20)
	c_description = models.TextField('Description')
	c_status = models.CharField('Status',max_length=25,choices=STATUS,default = 'Sent')
	c_deptno = models.ForeignKey(Hostel_office)
	c_date = models.DateField('Date',default = timezone.now())
	def __str__(self):
		return self.c_category

