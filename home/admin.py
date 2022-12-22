from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from home.models import (CustomUser, Realtor, Contact)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email", 
                    "phone",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "password1", "password2"), },), )
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
    ]
    ordering = ("first_name", "last_name")
    list_display_links = ["first_name", "email"]
    list_filter = ["created_at"]


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['user','gender', 'created_at']
    list_filter = ['gender','created_at']
    search_fields = ['user']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'listing']
    autocomplete_fields = ['listing','user']
    search_fields = ['user', 'name', 'email', 'listing']
    list_filter = ['created_at']
    date_heirarchy = 'created_at'
    # readonly_fields = ['listing']

