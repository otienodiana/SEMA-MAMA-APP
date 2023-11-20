from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    
    Roles=(
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Health_provider', 'Health_provider'),
        
    )
    role = models.CharField(max_length=20, choices=Roles)#(admin,health provider)

    REQUIRED_FIELDS = ['role', 'first_name', 'last_name']
# Create your models here.
#Customer Table
class Customer(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emailadress= models.CharField(max_length=255)
    profile_picture =models.ImageField(upload_to='landlord_profile_pic', blank=True,null=True)
    class Meta:
       db_table='Customer'

#Health provider table
class Health_provider(models.Model):
    Health_providerID = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emailadress= models.CharField(max_length=255)
    ROLE_TYPES = (
        (' Gynecologist ', ' Gynecologist '),
        (' Midwives', ' Midwives'),
        (' Psychologists', ' Psychologists'),
        ('Nurses:',  'Nurses:'),
        ('Peer_support', 'SelfPeer_support'),
    )
    role= models.CharField(max_length=20, choices=ROLE_TYPES)

    profile_picture =models.ImageField(upload_to='landlord_profile_pic', blank=True,null=True)
    class Meta:
       db_table='Health_provider'

#APOINTMENT TABLE
class Appointment (models.Model):
    
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    ROLE_TYPE = (
        ('Customer','Customer'),
        ('Health_provider','Health_provider'),
        
        
    )
    Role= models.CharField(max_length=20, choices=ROLE_TYPE,default='Meeting')
    
    APPOINTMENT_TYPE = (
        ('Check_up','Check_up'),
        ('Consultation','Consultation'),
        ('Mental_health','Mental_health'),
        ('Breastfeeding','Breastfeeding'),
        ('virtual_meetup','virtual _meetup'),
    )
    AppointmentType = models.CharField(max_length=20, choices=APPOINTMENT_TYPE)#(occupied, vacant, under maintenance)
    
    
    APPOINTMENT_STATUS = (
        ('Scheduled','Scheduled'),       
        ('Completed','Completed'),
        ('Canceled','Canceled'),
    )
    AppointmentStatus = models.CharField(max_length=20, choices=APPOINTMENT_STATUS,default='Scheduled')
    Comment = models.CharField(max_length=500)
    Date = models.DateTimeField(auto_now=True)


#INFORMATION/RESOURCES TABLES
class Resources(models.Model):
    ResourceID = models.ForeignKey
    DOCUMENT_TYPES = (
        ('Mental-health videos', 'Mental-health videos'),
        ('Articles', 'Articles'),
        ('Treatment Guides', 'Treatment Guides'),
        ('Resource Directories', 'Resource Directories'),
        ('User_guides', 'User_guides'),
    )
    ResourceType = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    UploadDate = models.DateTimeField


#pd screening table
class PD_SCREENING(models.Model):
    ID = models.IntegerField(primary_key=True),
    CustomerID =models.ForeignKey(Customer, on_delete=models.CASCADE),
    Date =models.DateField(),
    Results =models.TextField(max_length=200),
    SCREENING_TYPES = (
        ('Edinburgh Postnatal Depression Scale', 'Edinburgh Postnatal Depression Scale'),
        ('Patient Health Questionnaire', 'Patient Health Questionnaire'),
        ('Postpartum Depression Screening Scale', 'Postpartum Depression Screening Scale'),
        ('Beck Depression Inventory-II ', 'Beck Depression Inventory-II'),
        ('Zung Self-Rating Depression Scale ', 'Zung Self-Rating Depression Scale '),
    )
    Screening_tool = models.CharField(max_length=20, choices=SCREENING_TYPES)
    SCORE_TYPES = (
        ('0_10', '0_10'),
        ('11_20', '11_20'),
        ('21_30', '21_30 '),
        ('31_40', '31_40'),
        ('41-50', '41-50'),
        ('Above 50', 'Above 50'),

    )
    Score = models.CharField(max_length=20, choices=SCORE_TYPES)


#RESOURCE LOCATOR TABLE
class Resource_Locator(models.Model):
    Resource_LocatorID= models.IntegerField(primary_key=True),
    CustomerID =models.ForeignKey(Customer, on_delete=models.CASCADE),
    Health_Facility =models.CharField(max_length=250),
    Support_Groups =models.CharField(max_length=250),
    Location_details =models.CharField(max_length=250),



#FEEDBACK TABLE
class Feedback(models.Model):
    Feedback_ID= models.IntegerField(primary_key=True),
    CustomerID =models.ForeignKey(Customer, on_delete=models.CASCADE),
    Date =models.DateField(),
    Comments =models.CharField(max_length=250),
    RATING_TYPES = (
        ('Very satisfied', 'Very satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Unsatisfied', 'Unsatisfied '),
        

    )
    Ratings = models.CharField(max_length=20, choices=RATING_TYPES)
    Response_Status = models.BooleanField()