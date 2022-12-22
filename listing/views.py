from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from home.forms import ContactForm
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


class ListingDetailView(DetailView, FormView):
    template_name = 'listing/listing_detail.html'
    model = Listing
    context_object_name = "listing"
    form_class = ContactForm


    def get_queryset(self):
        queryset = Listing.items.select_related('realtor__user') \
            .filter(status=ListingStatus.Published)
        return queryset

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        form.fields['listing'].queryset = Listing.objects.filter(slug=self.object.slug)

        return form

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        if user.is_authenticated:
            initial.update({
                'name': user.get_full_name(),
                'email': user.email,
                'phone': user.phone,
            })
        initial.update({
                'listing': self.object.title,
            })
        return initial

    def form_valid(self, form):
        contact_form = form.save(commit=False)
        contact_form.listing = form.cleaned_data['listing']
        contact_form.save()
        realtor_email = self.object.realtor.user.email
        send_mail(
                subject=f"Property Listing Enquires for {form.cleaned_data['listing']}",
                message=f"{form.cleaned_data['message']}\n\nsign in to into the admin panel for more information",
                from_email="contact@btrealestate.co",
                recipient_list=[form.cleaned_data['email'], realtor_email],
            )
        if self.request.user.is_authenticated:
            contact_form = form.save(commit=False)
            contact_form.user = self.request.user
            contact_form.listing = form.cleaned_data['listing']
            contact_form.save()
            messages.success(self.request, "Your request has been submitted, A realtor will get back to you soon")
            return redirect(reverse_lazy('home:dashboard'))


        messages.success(self.request, "Your request has been submitted, A realtor will get back to you soon")
        return redirect('listing:listing-detail', self.kwargs.get('slug'))
                
