"""Django admin interface for profile_extrainfo models. """
from django.contrib import admin
from .models import *


class ProfileExtraInfoAdmin(admin.ModelAdmin):
    """Admin Interface for ProfileExtraInfo model."""

    raw_id_fields = ["user"]
    list_display = ["user", "country_code"]
    search_fields = ["user__username", "user__email"]


admin.site.register(ProfileExtraInfo, ProfileExtraInfoAdmin)
