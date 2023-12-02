"""
URL configuration for realEstateSoftware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from semaapp import views
from django.contrib.auth import views as auth_views


#WEB URL PATTERNS
urlpatterns = [
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logins', views.logins, name='logins'),
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('confirmappointment', views.confirmappointment, name='confirmappointment'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('resource_cards', views.resource_cards, name='resource_cards'),
    path('resource_detail/<int:ResourceID>', views.resource_detail, name='resource_detail'),
    path('view_source/<int:ResourceID>', views.view_source, name='view_source'),
    path('dashboard/<int:ResourceID>', views.dashboard, name='dashboard'),
    path('feedback', views.feedback, name='feedback'),
    path('confirmfeedback', views.confirmfeedback, name='confirmfeedback'),
    path('resource_locator', views.resource_locator, name='resource_locator'),
    path('PD_screening', views.PD_screening, name='PD_screening'),
    path('testing', views.testing, name='testing'),
    path('feedbacklist', views.feedbacklist, name='feedbacklist'),
    path('screenedlist', views.screenedlist, name='screenedlist'),
    path('confirmresource', views.confirmresource, name='confirmresource'),
]