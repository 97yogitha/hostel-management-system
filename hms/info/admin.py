from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Hostel_block
from .models import Room
from .models import Mess
from .models import Writes
from .models import Hostel_office
from .models import Complaint




admin.site.register(Student)
admin.site.register(Hostel_block)

admin.site.register(Mess)
admin.site.register(Room)
admin.site.register(Complaint)
admin.site.register(Writes)
admin.site.register(Hostel_office)
