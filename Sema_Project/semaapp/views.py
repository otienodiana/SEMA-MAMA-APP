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
from django.contrib.auth.models import User



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
         registers = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, role=role)
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
