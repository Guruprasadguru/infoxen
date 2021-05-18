from django.contrib import admin
from app.models import Lead
# Register your models here.

class LeadAdmin(admin.ModelAdmin):
    list_display = ['address','buisness_name','person_name','contact','verified_status','time_stamp']
from django.contrib import admin

# Register your models here.
admin.site.register(Lead,LeadAdmin)