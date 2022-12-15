from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import CustomUser, Contact
from realestate.utils.forms import CssForm


class CustomSignupForm(CssForm, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 
            'password2'
        ]


class ContactForm(CssForm, forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'listing',
            'name',
            'email',
            'phone',
            'message'

        ]