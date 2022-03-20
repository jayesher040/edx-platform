"""
Models for ProfileExtra Information

Migration Notes

If you make changes to this model, be sure to create an appropriate migration
file and check it in at the same time as your model changes. To do that,

1. Go to the edx-platform dir
2. ./manage.py lms makemigrations --settings=production profile_extrainfo
3. ./manage.py lms migrate --settings=production profile_extrainfo
"""
import logging

from model_utils.models import TimeStampedModel
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_noop
from django.contrib.auth.models import User
from django.conf import settings

from django_countries.fields import CountryField

log = logging.getLogger(__name__)


def get_or_none(classmodel, **kwargs):
    """
    Return object if exist otherwise return None
    """
    try:
        return classmodel.objects.get(**kwargs)
    except Exception as e:
        return None


class ProfileExtraInfo(TimeStampedModel):
    """
    Model for store user releted extra details
    """

    user = models.OneToOneField(
        User, unique=True, db_index=True, on_delete=models.CASCADE
    )
    country_code = models.CharField(max_length=255, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "ProfileExtraInfo"
        verbose_name_plural = "Profile Extra Info"

    @classmethod
    def create_or_update(cls, user_id, country_code):
        """
        Create or update User Details.
        """
        user, created = cls.objects.get_or_create(user_id=user_id)
        user.country_code = country_code
        user.save()
