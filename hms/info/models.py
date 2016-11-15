from __future__ import unicode_literals

from django.db import models

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
		return self.room_type
	
	

class Mess(models.Model):
	MESS_NAME = (('GH','girls hostel top mess'),
					('IH','girls hostel down mess'),
					('MM','Mega mess'),
					('FB','First Block mess'),
					('SB','Second Block mess'),
					('TB','Third Block mess'),
					)
	mess_name = models.CharField(max_length=25, choices = MESS_NAME,primary_key=True)
	per_day_cost = models.IntegerField()
	day = models.CharField(max_length=10)
	morning = models.TextField()
	afternoon = models.TextField()
	snacks = models.TextField()
	dinner = models.TextField()
	def __str__(self):
		return self.mess_name

class Room(models.Model):

	room_no = models.IntegerField()
	validity = models.DateField()
	block_no = models.ForeignKey(Hostel_block)
	def __str__(self):
		return self.room_no

class Student(models.Model):
	name = models.CharField(max_length=40)
	sem = models.IntegerField()
	dob = models.DateField()
	roll_no = models.CharField(max_length=6, unique=True,primary_key=True)
	reg_no = models.CharField(max_length=6,unique=True)
	hostel_feeno = models.CharField(max_length=6,unique=True)
	coll_feeno = models.CharField(max_length=6,unique=True)
	mess_no = models.IntegerField()
	branch = models.CharField(max_length=25)
	room_no = models.ForeignKey(Room)
	mess_names = models.ForeignKey(Mess)

	def __str__(self):
		return self.roll_no
class Hostel_office(models.Model):
	dept_no = models.IntegerField(primary_key=True)
	dept_name = models.CharField(max_length=25)

	def  __str__(self):
		return self.dept_name
		
class Complaint(models.Model):
	
	STATUS = (('Recieved','Recieved'),
				('In Progress','In Progress'),
				('Completed','Completed'),
				)
	c_no = models.IntegerField(primary_key=True)
	c_category = models.CharField(max_length=20)
	c_description = models.TextField()
	c_status = models.CharField(max_length=25,choices=STATUS)
	c_deptno = models.ForeignKey(Hostel_office)

class Writes(models.Model):

	w_rollno = models.ForeignKey(Student)
	w_cno = models.ForeignKey(Complaint)
	w_date = models.DateField()
