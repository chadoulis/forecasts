from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as the_time


class Profile(models.Model):

    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        'groups.CustomGroup', blank=True, related_name='group')

    def __str__(self):
        return u'Profile of User: {}'.format(self.user)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), max_length=255, unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    email = models.EmailField(_('Email address'), max_length=255, unique=True)
    date_joined = models.DateTimeField(_('Date joined'), default=the_time)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = auth.models.UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return u'{}'.format(self.username)

    def __repr__(self):
        return u'{}(id={}, first_name={}, last_name={})'.format(
            type(self).__name__, self.id, self.first_name, self.last_name)