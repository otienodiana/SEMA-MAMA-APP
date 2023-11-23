from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import  authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages, auth
# Importing the built-in User model
from . models import User,Appointment,Resources



# Create your views here.
#home page
def home(request):
   return render(request, 'home.html')

#REGSRATION VIEWTI
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname= request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        registerss = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password, role=role)
        return redirect('logins')


    return render(request, 'register.html')
#LOGIN PAGE
def logins(request):
    if request.method == 'POST':
        username = request.POST['username']  # Change 'email' to 'username'
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)  # Use 'username' instead of 'email'

        if user is not None:
            auth.login(request, user)  # Use 'auth.login' instead of 'auth_login'
            messages.success(request, 'Logged in successfully')
            return redirect('dashboard')  # Remove the trailing '/'
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
        
    
    return render(request, 'login.html')


#Appointment Form
def create_appointment(request):
    if request.method == 'POST':
        Firstname = request.POST['Firstname']
        Lastname= request.POST['Lastname']
        Role = request.POST['Role']
        AppointmentType = request.POST['AppointmentType']
        AppointmentStatus= request.POST['AppointmentStatus']
        Comment= request.POST['Comment']
        Date= request.POST['Date']  
        appointment= Appointment.objects.create(Firstname=Firstname, Lastname=Lastname, Role=Role, AppointmentType=AppointmentType, AppointmentStatus=AppointmentStatus,  Comment=Comment, Date=Date)
        
    return render(request,'appointment.html')

#CONFIRM APPOINTMENT
def confirmappointment(request):
    appoint = Appointment.objects.first()
    
    # Retrieve all properties as a queryset
    appointy = Appointment.objects.all()

    # Print the data (optional, for debugging purposes)
    print(appoint)
    # Handle the booking confirmation logic here
    # You can save the booking details to your database, send confirmation emails, etc.
    appoint = (Appointment)
    return render(request, 'confirmappointment.html', {'appoint': appoint})

#LIST OF APPOINTMENT
def appointmentlist(request):
    appoint = Appointment.objects.all()  # Retrieve all properties from the database
    return render(request, 'appointlist.html', {'appoint': appoint})



#LOGOUT CODE
def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='logins/')
def dashboard (request):
   user = request.user
   role = user.role
   properties = Appointment.objects.all()#[:3]
   context = {
       'properties': properties,
       'role': role,
   }
   return render(request, 'dashboard.html', context=context)

#RESOURCES VIEW
def resource_cards(request):
    source = Resources.objects.all()  # Fetch properties from your database
    paginator = Paginator(source, 4) 
    page = request.GET.get('page') 
    try:
        info=paginator.page(page)
    except PageNotAnInteger:
        info=paginator.page(1)
    except EmptyPage:
        info=paginator.page(paginator.num_pages)
     
    return render(request, 'cards.html', {'source':source, 'page':page})
