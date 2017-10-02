# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin ,BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **kwargs):
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
            is_staff=is_staff, is_active=True,
            is_superuser=is_superuser,
            firstname=kwargs.get('firstname', None),
            lastname=kwargs.get('lastname', None))

        account.set_password(password)
        account.save(using=self._db)

        return account

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, False, False,
                                 **kwargs)

    def create_superuser(self, email , password=None, **kwargs):
        return self._create_user(email, password, True, True,
                                 **kwargs)


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=30, blank=True , null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return ' '.join(self.firstname, self.last_login)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.firstname