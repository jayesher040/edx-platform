"""
    Manage signal handlers here
"""
import logging

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

log = logging.getLogger(__name__)
