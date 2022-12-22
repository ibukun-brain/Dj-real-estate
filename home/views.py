from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView
from home.models import Realtor, Contact
from listing.models import Listing
from realestate.utils.choices import ListingStatus, PriceChoices, BedRoomChoices, StateChoices
# Create your views here.



class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listings = Listing.objects.select_related('realtor__user') \
            .order_by('-created_at') \
            .filter(status=ListingStatus.Published)[:3]
        
        context.update({
        "listings":listings,
        'PriceChoices':PriceChoices,
        'BedRoomChoices':BedRoomChoices,
        'StateChoices':StateChoices,
        })

        return context

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mvp_realtor = Realtor.items.filter(is_mvp=True).first()
        realtors = Realtor.items.select_related('user').order_by('-created_at')
        context.update({
        "mvp_realtor":mvp_realtor,
        "realtors":realtors,
        })

        return context


class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'home/dashboard.html'
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 9

    def get_queryset(self):
        queryset = Contact.objects.order_by('created_at') \
            .filter(user=self.request.user)


        return queryset


class SearchView(TemplateView):
    template_name = 'home/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        listings = Listing.objects.select_related('realtor__user') \
            .order_by('-created_at') \
            .filter(status=ListingStatus.Published)
        
        keywords = request.GET.get('keywords')
        city = request.GET.get('city')
        state = request.GET.get('state')
        bedrooms = request.GET.get('bedrooms')
        price = request.GET.get('price')

        def is_validparam(param):
            return param != '' and param is not None

        if is_validparam(keywords):
            listings = listings.filter(description__icontains=keywords)
            
        if is_validparam(city):
            listings = listings.filter(city__iexact=city)

        if is_validparam(state):
            listings = listings.filter(state__iexact=state)

        if is_validparam(bedrooms):
            listings = listings.filter(bedrooms__lte=bedrooms)

        if is_validparam(price):
            listings = listings.filter(price__lte=price)
    

        context.update({
        'listings':listings,
        'PriceChoices':PriceChoices,
        'BedRoomChoices':BedRoomChoices,
        'StateChoices':StateChoices,
        'keywords':keywords,
        'bedrooms':bedrooms,
        'city':city,
        'price':price,
        'state':state,
        })

        return context
