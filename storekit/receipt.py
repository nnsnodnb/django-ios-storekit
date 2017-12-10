from django.conf import settings
from pyinapp import AppStoreValidator, InAppValidationError
from storekit.models import InApp, Receipt, Response, Purchase
import logging


def subscribe_receipt(receipt, sandbox):
    try:
        validator = AppStoreValidator(
            bundle_id=settings.STOREKIT_APP_BUNDLE_ID,
            sandbox=sandbox
        )

        try:
            purchases = validator.validate(
                receipt=receipt,
                password=settings.STOREKIT_PURCHASED_SECRET
            )
            _process_purchases(purchases)
            return True

        except InAppValidationError as e:
            logging.error(e)
            pass

    except AttributeError as e:
        logging.error(e)
        pass


def _process_purchases(purchases):
    _process(purchases) if isinstance(purchases, list) else _process(purchases)


def _process(purchases):
    for p in purchases:
        pass
