from django.http.response import HttpResponse
from storekit.errors import AppValidationError
from storekit.receipt import normal_receipt, subscribe_receipt


def receive_normal_receipt(request):
    if request.method == 'POST':
        try:
            _ = normal_receipt(receipt=request.POST['receipt_data'], sandbox=False)
        except AppValidationError or AttributeError:
            return HttpResponse(status=400)

        return HttpResponse(status=200)


def receive_subscribe_receipt(request):
    if request.method == 'POST':
        try:
            _ = subscribe_receipt(receipt=request.POST['receipt_data'], sandbox=False)
        except AppValidationError or AttributeError:
            return HttpResponse(status=400)

        return HttpResponse(status=200)
