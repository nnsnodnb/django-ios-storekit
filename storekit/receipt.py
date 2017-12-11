from django.conf import settings
from pyinapp import AppStoreValidator, InAppValidationError
from storekit.models import Purchase
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
            return _process(purchases)

        except InAppValidationError as e:
            logging.error(e)
            pass
        except AttributeError as e:
            # NotFound STOREKIT_PURCHASED_SECRET
            logging.error(e)
            pass

    except AttributeError as e:
        # NotFound STOREKIT_APP_BUNDLE_ID
        logging.error(e)
        pass


def _process(purchases) -> list:
    return list(
        map(
            lambda purchase: Purchase.parser(purchase), purchases
        )
    )
