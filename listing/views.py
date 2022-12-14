from django.shortcuts import render
from django.views.generic import ListView, DetailView
from listing.models import Listing
from realestate.utils.choices import ListingStatus


# Create your views here.
class ListingView(ListView):
    template_name = 'listing/listing.html'
    paginate_by = 9
    model = Listing
    context_object_name = "listings"

    def get_queryset(self):
        queryset = Listing.items.select_related('realtor__user') \
            .order_by('-created_at') \
            .filter(status=ListingStatus.Published)
        return queryset


class ListingDetailView(DetailView):
    template_name = 'listing/listing_detail.html'
    model = Listing
    context_object_name = "listing"

    def get_queryset(self):
        queryset = Listing.items.select_related('realtor__user') \
            .filter(status=ListingStatus.Published)
        return queryset
