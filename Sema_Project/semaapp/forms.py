from django import forms
from .models import Appointment
from django.contrib.auth.forms import AuthenticationForm





 #CREATING ALOGIN FORM
class LoginForm(AuthenticationForm):
    Email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    # You can customize other fields as needed
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )


#LOGINFORM
# forms.py (inside your app)
from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())




#MY APPOINTMENT FORM
class appointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'  # Use all fields from the Rental model


