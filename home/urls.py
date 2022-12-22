from django.urls import path
from home import views as home_views

app_name = "home"

urlpatterns = [
    path(
        "",
        view=home_views.IndexView.as_view(),
        name="index",
    ),
    path(
        "about-us/",
        view=home_views.AboutView.as_view(),
        name="about",
    ),
    path(
        "dashboard/",
        view=home_views.DashboardView.as_view(),
        name="dashboard",
    ),
    path(
        "search/",
        view=home_views.SearchView.as_view(),
        name="search",
    )
]