from django.http import HttpResponse
from django.http.response import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json
import requests


@require_POST
@csrf_exempt
def subscribe_receipt(request):
    body = json.loads(request.body.decode('utf-8'))
    if 'sandbox' in body and 'receipt' in body:
        return HttpResponse(status=400)

    response = requests.post('https://sandbox.itunes.apple.com/verifyReceipt'
                             if body['sandbox'] else 'https://buy.itunes.apple.com/verifyReceipt',
                             data=json.dumps({'receipt-data': body['receipt'],
                                              'password': settings.STOREKIT_PURCHASED_SECRET
                                              if settings.STOREKIT_PURCHASED_SECRET != '' else ''})
                             ).json()
    if response['status'] != 0 and response['status'] != 21006:
        return HttpResponse()

    if response['latest_receipt_info'] is None:
        return HttpResponse(status=200)

    expires_date_ms = 0
    for info in response['latest_receipt_info']:
        if info['product_id'] is None or info['expires_date_ms'] is None:
            continue
        expires_date_ms = expires_date_ms \
            if expires_date_ms > int(info['expires_date_ms']) else int(info['expires_date_ms'])

    return JsonResponse({'expire': expires_date_ms / 1000})
