from django.conf import settings

from .appstore import AppStoreValidator


def normal_receipt(receipt, sandbox):
    try:
        storekit_bundle_id = settings.STOREKIT_APP_BUNDLE_ID
    except AttributeError:
        raise AttributeError('Please set "STOREKIT_APP_BUNDLE_ID" in your settings.py')

    validator = AppStoreValidator(bundle_id=storekit_bundle_id, sandbox=sandbox)

    return validator.validate(receipt=receipt)


def subscribe_receipt(receipt, sandbox):
    try:
        storekit_app_bundle_id = settings.STOREKIT_APP_BUNDLE_ID
    except AttributeError:
        raise AttributeError('Please set "STOREKIT_APP_BUNDLE_ID" in your settings.py')

    try:
        storekit_purchased_secret = settings.STOREKIT_PURCHASED_SECRET
    except AttributeError:
        raise AttributeError('Please set "STOREKIT_PURCHASED_SECRET" in your settings.py')

    validator = AppStoreValidator(bundle_id=storekit_app_bundle_id, sandbox=sandbox)

    return validator.validate(receipt=receipt, password=storekit_purchased_secret)
