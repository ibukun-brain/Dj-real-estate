from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import CustomUser, Contact
from listing.models import Listing
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
    listing = forms.ModelChoiceField(
       queryset=Listing.objects.none(),
       empty_label=None,
       widget=forms.Select(
            attrs={
                # 'readonly': True,

            }
       )
    )
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'message'

        ]

        labels = {
            'listing': 'property',
        }

        widgets = { 
            'message': forms.Textarea(
                attrs={
                    'rows':3,
                    'cols':20,
                }
            )
        }