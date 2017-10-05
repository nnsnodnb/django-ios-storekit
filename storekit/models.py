from django.db import models
from django.utils.timezone import now


class Purchase(models.Model):

    expires_date = models.IntegerField(blank=False, default=0)
    create_date = models.DateTimeField(blank=False, default=now)

    def __str__(self):
        return ''
