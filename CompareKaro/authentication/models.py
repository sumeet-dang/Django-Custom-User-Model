from django.db import models

import re
import uuid
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,
                                        BaseUserManager)
from django import forms
# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser,
                        **kwargs ):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username = username, email = email,
            is_staff = is_staff, is_superuser = is_superuser, last_login = now,
            date_joined = now, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **kwargs):
        return self._create_user(username, email, password, False, False,
            **kwargs)


    def create_superuser(self, username, email, password, **kwargs):
        user = self._create_user(username, email, password, True, True,
            **kwargs)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(_('username'), max_length=30,unique=True,
        help_text=_("""Required. 30 Characters or less, Letters
        Numbers or @.+-_ characters"""),
        validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        _('Enter a valid username'), _('invalid username'))])
    first_name = models.CharField(_('first_name'),
        max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last_name'),
        max_length=30, blank=True, null=True)
    email = models.CharField(_('Email address'),max_length=255)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text = _('Can Log into Admin Site'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text = _('Unselect to deactivate account'))
    date_joined = models.DateTimeField(_('Date Joined'),
        default= timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        return self.first_name
