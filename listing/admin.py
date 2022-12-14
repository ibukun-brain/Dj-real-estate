from django.contrib import admin
from listing.models import Listing
from realestate.utils.choices import ListingStatus

# Register your models here.
def publish_listings(modeladmin, rquest,queryset):
    queryset.update(status=ListingStatus.Published)  
publish_listings.short_description = 'Mark selected listings as published' 

def pend_listings(modeladmin, rquest,queryset):
    queryset.update(status=ListingStatus.Pending)  

pend_listings.short_description = 'Mark selected listings as pending'     

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'price', 'status', 'created_at', 'realtor']
    autocomplete_fields = ['realtor']
    list_filter = ['status', 'created_at', 'realtor']
    search_fields = ['title', 'address', 'realtor', 'state', 'city']
    actions = [publish_listings, pend_listings]