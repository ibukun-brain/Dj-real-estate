from django.urls import path
from listing import views as listing_views

app_name = "listing"

urlpatterns = [
    path(
        "",
        view=listing_views.ListingView.as_view(),
        name="listing-list"
    ),
    path(
        "<slug:slug>/",
        view=listing_views.ListingDetailView.as_view(),
        name="listing-detail"
    )
]