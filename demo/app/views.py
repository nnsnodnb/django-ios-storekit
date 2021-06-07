import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from storekit.errors import AppValidationError
from storekit.receipt import normal_receipt, subscribe_receipt


@csrf_exempt
def receive_normal_receipt(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            _ = normal_receipt(receipt=body["receipt-data"], sandbox=True)
        except AppValidationError or AttributeError:
            return HttpResponse(status=400)

        return HttpResponse(status=200)


@csrf_exempt
def receive_subscribe_receipt(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            _ = subscribe_receipt(receipt=body["receipt-data"], sandbox=True)
        except AppValidationError or AttributeError:
            return HttpResponse(status=400)

        return HttpResponse(status=200)
