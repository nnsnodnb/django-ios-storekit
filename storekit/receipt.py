from django.conf import settings

import json
import requests


def subscribe_receipt(receipt: str, sandbox: bool) -> {str: int}:
    url = 'https://sandbox.itunes.apple.com/verifyReceipt' if sandbox else 'https://buy.itunes.apple.com/verifyReceipt'
    response = requests.post(
        url=url,
        data=json.dumps({
            'receipt-data': receipt,
            'password': settings.STOREKIT_PURCHASED_SECRET if settings.STOREKIT_PURCHASED_SECRET != '' else ''
        })
    ).json()

    if response['status'] != 0 and response['status'] != 21006:
        return None

    if response['latest_receipt_info'] is None:
        return None

    expires_date_ms = 0
    for info in response['latest_receipt_info']:
        if info['product_id'] is None or info['expires_date_ms'] is None:
            continue
        expires_date_ms = expires_date_ms \
            if expires_date_ms > int(info['expires_date_ms']) else int(info['expires_date_ms'])

    return {'expire': expires_date_ms / 1000}
