from django.contrib import admin
from .models import *

class registerAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','password','profile','address')
admin.site.register(register,registerAdmin)

class contactusAdmin(admin.ModelAdmin):
    list_display=('Query','Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin,)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('Rating','Name','Email','Mobile','Message')
admin.site.register(feedback,FeedbackAdmin,)


class RailwayStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')  # Specify which fields to display in the admin list view
    search_fields = ('name', 'code') 
admin.site.register(RailwayStation,RailwayStationAdmin,)


class BookingAdmin(admin.ModelAdmin):
    list_display=('train_number','class_type','station_from','station_to','name','age','gender','pnr','date')
admin.site.register(Booking,BookingAdmin) 