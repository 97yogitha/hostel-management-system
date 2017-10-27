from django.db import models
from django.http import StreamingHttpResponse
from django.views.generic import View
from info.models import Mess
import csv
class Echo(object):
    """An object that implements just the write method of the file-like interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value
class ContactLogExportCsvView(View):
    def get(self, request, *args, **kwargs):
        Messs_qs = Mess.objects.all() # Assume 50,000 objects inside
        model = Messs_qs.model
        model_fields = mess._meta.fields + mess._meta.many_to_many
        headers = [field.name for field in model_fields] # Create CSV headers
        def get_row(mess):
            row = []
            for field in model_fields:
                if type(field) == models.ForeignKey:
                    val = getattr(obj, field.name)
                    if val:
                        val = val.__unicode__()
                elif type(field) == models.ManyToManyField:
                    val = u', '.join([item.__unicode__() for item in getattr(obj, field.name).all()])
                elif field.choices:
                    val = getattr(obj, 'get_%s_display'%field.name)()
                else:
                    val = getattr(obj, field.name)
                row.append(unicode(val).encode("utf-8"))
            return row
        def stream(headers, data): # Helper function to inject headers
            if headers:
                yield headers
            for obj in data:
                yield get_row(obj)
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        response = StreamingHttpResponse(
            (writer.writerow(row) for row in stream(headers, Messs_qs)),
            content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="all_Messs.csv"'
        return response


def export_csv(modeladmin, request, Mess.objects.all()):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mess.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"Name"),
        smart_str(u"Per dat"),
        smart_str(u"Description"),
    ])
    for obj in mess:
        writer.writerow([
            smart_str(obj.mess_name),
            smart_str(obj.per_day_cost),
        ])
    return response
export_csv.short_description = u"Export CSV"

import csv
from info.models import MessMenu
from django.utils.encoding import smart_str
mess = MessMenu.objects.all()
with open('yogitha.csv','wb') as f:  
    fieldnames = ['Mess Name','Day','Morning','Snacks']
    writer = csv.DictWriter('yogitha.csv', fieldnames=fieldnames)
    writer.writeheader()
   # writer.writerow(['Mess Name','Day','Morning','Snacks'])
    for obj in mess:
                    writer.writerow([
                        smart_str(obj.mess_name),smart_str(obj.day),smart_str(obj.morning),smart_str(obj.snacks)               
                    ])


from django.contrib import admin
from recruitments import models
from django.utils.encoding import smart_str
import csv
resume = models.Resume.objects.all()
with open('full_resume_list.csv','wb') as f:  
    #fieldnames = ['Name','Roll number','gender','Phone number','Email id','About me','Why IE','About me','Why IE','Event participation','Core Sig','2nd Sig pref','Projects','Script','Robotics','Video','P$
    #writer = csv.DictWriter('full_resume_list.csv', fieldnames=fieldnames)
    #writer.writeheader()
        writer=csv.writer(f)
        writer.writerow(['Name','Roll number','gender','Phone number','Email id','About me','Why IE','About me','Why IE','Event participation','Core Sig','2nd Sig pref','Projects','Script','Robotics','Vid$
for obj in resume:
        writer.writerow([ 
                smart_str(obj.name),
                smart_str(obj.roll_number),
                smart_str(obj.gender),
                smart_str(obj.phone_number),
                smart_str(obj.email.ed),
                smart_str(obj.about_me),
                smart_str(obj.why_ie),
                smart_str(event_participation),
                smart_str(obj.core_sig_choice),
                smart_str(obj.core_sig_choice_2),
                smart_str(obj.core_sig_projects),
                smart_str(obj.script_essay),
                smart_str(obj.robotics_essay),
                smart_str(obj.video)
                ]) 


from django.contrib import admin
from recruitments import models
from django.utils.encoding import smart_str
import csv
resume = models.Resume.objects.all()
with open('full_resume_list.csv','wb') as f:  
    #fieldnames = ['Name','Roll number','gender','Phone number','Email id','About me','Why IE','About me','Why IE','Event participation','Core Sig','2nd Sig pref','Projects','Script','Robotics','Video','P$
    #writer = csv.DictWriter('full_resume_list.csv', fieldnames=fieldnames)
    #writer.writeheader()
    writer=csv.writer(f)
    writer.writerow(['Name','Roll number','gender','Phone number','Email id','Core Sig','2nd Sig pref','Script','Robotics','Video'])
for obj in resume:
    writer.writerow([smart_str(obj.name),smart_str(obj.roll_number),smart_str(obj.gender),smart_str(obj.phone_number),smart_str(obj.email.ed),smart_str(obj.core_sig_choice),smart_str(obj.core_sig_choice_2),smart_str(obj.core_sig_projects),smart_str(obj.script_essay),smart_str(obj.robotics_essay),smart_str(obj.video)]) 


