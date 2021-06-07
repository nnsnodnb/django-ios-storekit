import requests

from .errors import AppValidationError
from .models import Response

api_result_ok = 0
api_result_errors = {
    21000: "Bad json",
    21002: "Bad data",
    21003: "Receipt authentication",
    21004: "Shared secret mismatch",
    21005: "Server is unavailable",
    21006: "Subscription has expired",
    21007: "Sandbox receipt was sent to the production env",
    21008: "Production receipt was sent to the sandbox env",
}


class AppStoreValidator(object):
    def __init__(self, bundle_id, sandbox=False):
        self.bundle_id = bundle_id

        if sandbox:
            self.url = "https://sandbox.itunes.apple.com/verifyReceipt"
        else:
            self.url = "https://buy.itunes.apple.com/verifyReceipt"

    def validate(self, receipt, password=None):
        receipt_json = {"receipt-data": receipt}
        if password:
            receipt_json["password"] = password

        api_response = requests.post(self.url, json=receipt_json).json()

        status = api_response["status"]

        if status != api_result_ok:
            error = AppValidationError(api_result_errors.get(status, "Unknown API status"), api_response)
            raise error

        purchases = self._parse_receipt(api_response)
        return purchases

    def _parse_receipt(self, api_response):
        if self.bundle_id != api_response["receipt"]["bundle_id"]:
            raise AppValidationError("Bundle ID mismatch", api_response)
        return [Response.parser(api_response, in_app) for in_app in api_response["receipt"]["in_app"]]
