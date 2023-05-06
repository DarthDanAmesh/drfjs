import os
import sys

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as UserManagerBase
from django.utils import timezone

if "makemigrations" in sys.argv:
    from django.utils.translation import gettext_noop as _
else:
    from django.utils.translation import gettext_lazy as _

JOB_TYPES = (
    ('Full Time', 'Full Time'),
    ('Contract', 'Contract Time'),
    ('Internship', 'Internship'),
    ('Industrial Attachment', 'Industrial Attachment'),
)

EXPERIENCE_LEVEL = [
    ('ENTRY-LEVEL', 'ENTRY-LEVEL'),
    ('INTERMEDIATE-LEVEL', 'INTERMEDIATE-LEVEL'),
    ('MID-LEVEL', 'MID-LEVEL'),
    ('SENIOR OR EXECUTIVE-LEVEL', 'SENIOR OR EXECUTIVE-LEVEL'),
]

COUNTIES_LIST = (
    ('1', 'Mombasa'), ('2', "Nairobi"), ('3', 'Kisumu'), ('4', 'Nakuru'), ('5', 'Namanga'),
    ('6', 'Kilifi'), ('7', 'Kwale'), ('8', 'Eldoret'), ('9', 'Moyale'), ('10', 'Busia'),
)


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class UserManager(UserManagerBase):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not username:
            username = email
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not username:
            username = email
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    # change username to non-editable non-required field
    username = models.CharField(
        _("username"), max_length=150, editable=False, blank=True
    )
    # change email to unique and required field
    email = models.EmailField(_("email address"), unique=True)
    cover = models.FileField(_("cover letter"), upload_to=upload_to, blank=True)
    resume = models.FileField(_("resume"), upload_to=upload_to, blank=True)
    id_number = models.CharField(max_length=50, default='777')
    middle_name = models.CharField(max_length=150, default='777')
    first_two_names = models.CharField(max_length=150)
    contact = models.CharField(max_length=20, default='777')
    location = models.CharField(max_length=50, default='Nairobi')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
