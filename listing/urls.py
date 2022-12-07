from django.urls import path
from listing import views as listing_views

app_name = "listing"

urlpatterns = [
    path(
        "",
        view=listing_views.ListingView.as_view(),
        name="listing-list"
    )
]