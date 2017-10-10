from django.conf import settings
from pyinapp import AppStoreValidator, InAppValidationError


validator = AppStoreValidator(settings.STOREKIT_APP_BUNDLE_ID)


def subscribe_receipt(receipt):
    try:
        purchases = validator.validate(receipt)
        process_purchases(purchases)
    except InAppValidationError:
        """ handle validation error """


def process_purchases(purchases):
    process(*purchases) if isinstance(purchases, list) else process(purchases)


def process(*purchases):
    for p in purchases:
        """ for instance, save p to db and add a player some coins for it """
