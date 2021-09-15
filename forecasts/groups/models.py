from django.db import models

from forecasts.utils.unique import get as get_random

class CustomGroup(models.Model):
    name = models.CharField(max_length=50, default='MyGroup',null=False,
                            blank=False)

    created_on = models.DateTimeField(auto_now_add=True)

    guid = models.CharField(unique=True, max_length=50,
                            default=get_random, editable=False)

    def __str__(self):
        return u'{}'.format(self.name)