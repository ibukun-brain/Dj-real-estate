from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ListingView(TemplateView):
    template_name = 'listing/listing.html'
