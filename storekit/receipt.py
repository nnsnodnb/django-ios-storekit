from django.conf import settings
from pyinapp import AppStoreValidator, InAppValidationError


def subscribe_receipt(receipt, sandbox):
    validator = AppStoreValidator(
        bundle_id=settings.STOREKIT_APP_BUNDLE_ID,
        sandbox=sandbox
    )
    try:
        purchases = validator.validate(receipt)
        process_purchases(purchases)
    except InAppValidationError:
        """ handle validation error """


def process_purchases(purchases):
    process(*purchases) if isinstance(purchases, list) else process(purchases)


def process(*purchases):
    for p in purchases:
        print(p['aaa'])
