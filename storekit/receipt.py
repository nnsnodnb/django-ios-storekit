from django.conf import settings
from .appstore import AppStoreValidator
from .errors import AppValidationError
from .models import Purchase
import logging


def normal_receipt(receipt, sandbox):
    try:
        validator = AppStoreValidator(
            bundle_id=settings.STOREKIT_APP_BUNDLE_ID,
            sandbox=sandbox
        )

        try:
            return validator.validate(
                receipt=receipt
            )

        except AppValidationError as e:
            logging.error(e)
            raise

    except AttributeError as e:
        # NotFound STOREKIT_APP_BUNDLE_ID
        logging.error(e)
        raise


def subscribe_receipt(receipt, sandbox):
    try:
        validator = AppStoreValidator(
            bundle_id=settings.STOREKIT_APP_BUNDLE_ID,
            sandbox=sandbox
        )

        try:
            return validator.validate(
                receipt=receipt,
                password=settings.STOREKIT_PURCHASED_SECRET
            )

        except AppValidationError as e:
            logging.error(e)
            raise

        except AttributeError as e:
            # NotFound STOREKIT_PURCHASED_SECRET
            logging.error(e)
            raise

    except AttributeError as e:
        # NotFound STOREKIT_APP_BUNDLE_ID
        logging.error(e)
        raise
