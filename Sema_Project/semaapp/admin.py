from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ['username', "first_name", "last_name", "role",]
    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('personal Info', {'fields': ('email', 'first_name', 'last_name', 'role')}),
        ('permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2', 'first_name', 'last_name',
                           'email', 'is_staff', 'is_active', 'role')}),
    )
    

#For property
admin.site.register(User, UserAdmin)

#for customers
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "firstname", "lastname", "emailadress", "CustomerID",
         "profile_picture"
    )

admin.site.register(Customer, CustomerAdmin)

#Foe health providers
class Health_providerAdmin(admin.ModelAdmin):
    list_display = (
        "firstname", "lastname", "emailadress", "Health_providerID",
         "profile_picture", "role"
    )

admin.site.register(Health_provider, Health_providerAdmin)


#For apointment table
class appointmentAdmin(admin.ModelAdmin):
    list_display = (
        "Firstname", "Lastname", "Role", "AppointmentType",
         "AppointmentStatus","Comment","Date"
    )
admin.site.register(Appointment,appointmentAdmin )

#For Resources
class ResourcesAdmin(admin.ModelAdmin):
    list_display = (
        "ResourceID","ResourceType", "UploadDate",
"File",
    )

admin.site.register(Resources, ResourcesAdmin)

#For Screening
class PD_SCREENINGAdmin(admin.ModelAdmin):
    list_display = (
        "ID","CustomerID", "Date","Results","Screening_tool","Score",
    )

admin.site.register(PD_SCREENING, PD_SCREENINGAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "Feedback_ID","CustomerID", "Date","Comments","Ratings","Response_Status",
    )

admin.site.register(Feedback, FeedbackAdmin)
