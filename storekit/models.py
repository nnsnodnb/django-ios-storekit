from django.db import models
from django.utils.timezone import now


class Purchase(models.Model):
    transaction_id = models.CharField(blank=False, default='', max_length=255)
    product_id = models.CharField(blank=False, default='', max_length=255)
    quantity = models.IntegerField(blank=False, default=0)
    purchase_date = models.CharField(blank=False, default='', max_length=255)

    def __str__(self):
        return 'transaction_id: ' + self.transaction_id
