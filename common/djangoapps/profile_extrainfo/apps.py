"""
ProfileExtrainfo Application Configuration

ProfileExtrainfo Application signal handlers are connected here.
"""

from django.apps import AppConfig


class ProfileExtrainfoConfig(AppConfig):
    """
    Application Configuration for ProfileExtrainfo app.
    """

    name = "common.djangoapps.profile_extrainfo"
    verbose_name = "User Profile Extra Info"

    def ready(self):
        """
        Connect handlers to signals.
        """
        # Can't import models at module level in AppConfigs, and models get
        # included from the signal handlers
        from .signals import handlers  # pylint: disable=unused-variable
