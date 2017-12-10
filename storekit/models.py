from django.db import models


class InApp(models.Model):
    quantity = models.IntegerField(blank=True)
    product_id = models.CharField(blank=False, default='', max_length=255)
    transaction_id = models.IntegerField(blank=True)
    original_transaction_id = models.IntegerField(blank=True)
    purchase_date = models.CharField(blank=False, default='', max_length=255)
    purchase_date_ms = models.IntegerField(blank=True)
    purchase_date_pst = models.CharField(blank=False, default='', max_length=255)
    original_purchase_date = models.CharField(blank=False, default='', max_length=255)
    original_purchase_date_ms = models.IntegerField(blank=True)
    original_purchase_date_pst = models.CharField(blank=False, default='', max_length=255)
    is_trial_period = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return '{}: {}'.format(self.product_id, self.quantity)

    def __repr__(self):
        return '{} <ID: {}>: "{}"'.format(self.product_id, self.id, self.__class__.__name__)


class Receipt(models.Model):
    receipt_type = models.CharField(blank=False, default='', max_length=255)
    adam_id = models.IntegerField(blank=True)
    app_item_id = models.IntegerField(blank=True)
    bundle_id = models.CharField(blank=False, default='', max_length=255)
    application_version = models.CharField(blank=False, default='', max_length=255)
    download_id = models.IntegerField(blank=True)
    version_external_identifier = models.IntegerField(blank=True)
    receipt_creation_date = models.CharField(blank=False, default='', max_length=255)
    receipt_creation_date_ms = models.IntegerField(blank=True)
    receipt_creation_date_pst = models.CharField(blank=False, default='', max_length=255)
    request_date = models.CharField(blank=False, default='', max_length=255)
    request_date_ms = models.IntegerField(blank=True)
    request_date_pst = models.CharField(blank=False, default='', max_length=255)
    original_purchase_date = models.CharField(blank=False, default='', max_length=255)
    original_purchase_date_ms = models.IntegerField(blank=True)
    original_purchase_date_pst = models.CharField(blank=False, default='', max_length=255)
    original_application_version = models.CharField(blank=False, default='', max_length=255)
    in_app = models.ForeignKey(InApp, blank=True)

    def __str__(self):
        return '【{}】{}: {}'.format(self.receipt_type, self.bundle_id, self.application_version)

    def __repr__(self):
        return '<ID: {}>: "{}"'.format(self.id, self.__class__.__name__)


class Response(models.Model):
    status = models.IntegerField(blank=True)
    environment = models.CharField(blank=False, default='', max_length=255)
    receipt = models.ForeignKey(Receipt, blank=True)

    def __str__(self):
        return 'Response: ' + self.environment

    def __repr__(self):
        return '<ID: {}>: "{}"'.format(self.id, self.__class__.__name__)


class Purchase(models.Model):
    transaction_id = models.IntegerField(blank=True)
    product_id = models.IntegerField(blank=True)
    quantity = models.IntegerField(blank=False, default=0)
    purchased_at = models.CharField(blank=False, default='', max_length=255)
    response = models.ForeignKey(Response, blank=True)

    def __str__(self):
        return 'Purchase: ' + str(self.transaction_id)

    def __repr__(self):
        return '{} <ID: {}>: "{}"'.format(self.product_id, self.id, self.__class__.__name__)
