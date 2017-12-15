from django.db import models
from pyinapp.purchase import Purchase as LibPurchase


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

    def __init__(self, quantity, product_id, transaction_id, original_transaction_id,
                 purchase_date, purchase_date_ms, purchase_date_pst, original_purchase_date,
                 original_purchase_date_ms, original_purchase_date_pst, is_trial_period):
        super(InApp, self).__init__(quantity, product_id, transaction_id, original_transaction_id, purchase_date,
                                    purchase_date_ms, purchase_date_pst, original_purchase_date,
                                    original_purchase_date_ms, original_purchase_date_pst, is_trial_period)
        self.quantity = quantity
        self.product_id = product_id
        self.transaction_id = transaction_id
        self.original_transaction_id = original_transaction_id
        self.purchase_date = purchase_date
        self.purchase_date_ms = purchase_date_ms
        self.purchase_date_pst = purchase_date_pst
        self.original_purchase_date = original_purchase_date
        self.original_purchase_date_ms = original_purchase_date_ms
        self.original_purchase_date_pst = original_purchase_date_pst
        self.is_trial_period = is_trial_period

    def __str__(self):
        return '{}: {}'.format(self.product_id, self.quantity)

    def __repr__(self):
        return '{} <ID: {}>: "{}"'.format(self.product_id, self.id, self.__class__.__name__)

    @classmethod
    def parser(cls, json, is_save=True):
        in_app = {
            'quantity': int(json['quantity']),
            'product_id': json['product_id'],
            'transaction_id': int(json['transaction_id']),
            'original_transaction_id': int(json['original_transaction_id']),
            'purchase_date': json['purchase_date'],
            'purchase_date_ms': int(json['purchase_date_ms']),
            'purchase_date_pst': json['purchase_date_pst'],
            'original_purchase_date': json['original_purchase_date'],
            'original_purchase_date_ms': int(json['original_purchase_date_ms']),
            'original_purchase_date_pst': json['original_purchase_date'],
            'is_trial_period': bool(json['is_trial_period'])
        }
        obj = cls(**in_app)
        if is_save:
            obj.save()
        return obj


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

    def __init__(self, receipt_type, adam_id, app_item_add, bundle_id,
                 application_version, download_id, version_external_identifier,
                 receipt_creation_date, receipt_creation_date_ms, receipt_creation_date_pst,
                 request_date, request_date_ms, request_date_pst, original_purchase_date,
                 original_purchase_date_ms, original_purchase_date_pst, original_application_version,
                 in_app: InApp):
        super(Receipt, self).__init__(receipt_type, adam_id, app_item_add, bundle_id, application_version, download_id,
                                      version_external_identifier, receipt_creation_date, receipt_creation_date_ms,
                                      receipt_creation_date_pst, request_date, request_date_ms, request_date_pst,
                                      original_purchase_date, original_purchase_date_ms, original_purchase_date_pst,
                                      original_application_version, in_app)

    def __str__(self):
        return '【{}】{}: {}'.format(self.receipt_type, self.bundle_id, self.application_version)

    def __repr__(self):
        return '<ID: {}>: "{}"'.format(self.id, self.__class__.__name__)

    @classmethod
    def parser(cls, json, is_save=True):
        receipt = {
            'receipt_type': json['receipt_type'],
            'adam_id': int(json['adam_id']),
            'app_item_id': int(json['app_item_id']),
            'bundle_id': json['bundle_id'],
            'application_version': json['application_version'],
            'download_id': int(json['download_id']),
            'version_external_identifier': int(json['version_external_identifier']),
            'receipt_creation_date': json['receipt_creation_date'],
            'receipt_creation_date_ms': int(json['receipt_creation_date_ms']),
            'receipt_creation_date_pst': json['rceipt_creation_date_pst'],
            'request_date': json['request_date'],
            'request_date_ms': int(json['request_date_ms']),
            'request_date_pst': json['request_date_pst'],
            'original_purchase_date': json['original_purchase_date'],
            'original_purchase_date_ms': int(json['original_purchase_date_ms']),
            'original_purchase_date_pst': json['original_purchase_date_pst'],
            'in_app': InApp.parser(json['in_app'])
        }
        obj = cls(**receipt)
        if is_save:
            obj.save()
        return obj


class Response(models.Model):
    status = models.IntegerField(blank=True)
    environment = models.CharField(blank=False, default='', max_length=255)
    receipt = models.ForeignKey(Receipt, blank=True)

    def __init__(self, status, environment, receipt):
        super(Response, self).__init__(status, environment, receipt)
        self.status = status
        self.environment = environment
        self.receipt = receipt

    def __str__(self):
        return 'Response: ' + self.environment

    def __repr__(self):
        return '<ID: {}>: "{}"'.format(self.id, self.__class__.__name__)

    @classmethod
    def parser(cls, json, is_save=True):
        response = {
            'status': json['status'],
            'environment': json['environment'],
            'receipt': Receipt.parser(json['receipt'])
        }
        obj = cls(**response)
        if is_save:
            obj.save()
        return obj


class Purchase(models.Model, LibPurchase):
    transaction_id = models.IntegerField(blank=True)
    product_id = models.IntegerField(blank=True)
    quantity = models.IntegerField(blank=False, default=0)
    purchased_at = models.CharField(blank=False, default='', max_length=255)
    response = models.ForeignKey(Response, blank=True)

    def __init__(self, transaction_id, product_id, quantity, purchased_at, response: Response):
        super(Purchase, self).__init__(transaction_id, product_id, quantity, purchased_at, response)
        super(LibPurchase, self).__init__()
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchased_at = purchased_at
        self.response = response

    def __str__(self):
        return 'Purchase: ' + str(self.transaction_id)

    def __repr__(self):
        return '{} <ID: {}>: "{}"'.format(self.product_id, self.id, self.__class__.__name__)

    @classmethod
    def parser(cls, json, is_save=True):
        purchase = {
            'transaction_id': json['transaction_id'],
            'product_id': json['product_id'],
            'quantity': int(json['quantity']),
            'purchased_at': json['purchased_at'],
            'response': Response.parser(json['response'])
        }
        obj = cls(**purchase)
        if is_save:
            obj.save()
        return obj
