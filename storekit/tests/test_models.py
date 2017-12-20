from unittest import TestCase
from storekit.models import InApp, Receipt, Response, Purchase

import json
import os.path


JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'response.json')


class InAppTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())['response']['receipt']['in_app'][0]

    def tearDown(self):
        self.response = None

    def test_new_data_save_true(self):
        in_app = InApp.parser(
            self.response
        )
        self.assertTrue(in_app)

    def test_new_data_save_false(self):
        in_app = InApp.parser(
            self.response,
            is_save=False
        )
        self.assertTrue(in_app)

    def test_str(self):
        in_app = InApp.parser(
            self.response
        )
        self.assertEqual(str(in_app), '{}: {}'.format(in_app.product_id, in_app.quantity))

    def test_repr(self):
        in_app = InApp.parser(
            self.response
        )
        self.assertEqual(repr(in_app),
                         '{} <ID: {}>: "{}"'.format(in_app.product_id, in_app.id, in_app.__class__.__name__))


class ReceiptTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())['response']['receipt']
            self.in_app = self.response['in_app'][0]

    def tearDown(self):
        self.response = None
        self.in_app = None

    def test_new_data_save_true(self):
        receipt = Receipt.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertTrue(receipt)

    def test_new_data_save_false(self):
        receipt = Receipt.parser(
            self.response,
            in_app=self.in_app,
            is_save=False
        )
        self.assertTrue(receipt)

    def test_str(self):
        receipt = Receipt.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(str(receipt),
                         '[{}] {}: {}'.format(receipt.receipt_type, receipt.bundle_id, receipt.application_version))

    def test_repr(self):
        receipt = Receipt.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(repr(receipt),
                         '<ID: {}>: "{}"'.format(receipt.id, receipt.__class__.__name__))


class ResponseTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())['response']
            self.in_app = self.response['receipt']['in_app'][0]

    def tearDown(self):
        self.response = None
        self.in_app = None

    def test_new_data_save_true(self):
        response = Response.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertTrue(response)

    def test_new_data_save_false(self):
        response = Response.parser(
            self.response,
            in_app=self.in_app,
            is_save=False
        )
        self.assertTrue(response)

    def test_str(self):
        response = Response.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(str(response),
                         'Response: ' + response.environment)

    def test_repr(self):
        response = Response.parser(
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(repr(response),
                         '<ID: {}>: "{}"'.format(response.id, response.__class__.__name__))


class PurchaseTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.receipt = json.loads(f.read())
            self.response = self.receipt['response']
            self.in_app = self.response['receipt']['in_app'][0]

    def tearDown(self):
        self.response = None
        self.in_app = None

    def test_new_data_save_true(self):
        purchase = Purchase.parser(
            self.receipt,
            self.response,
            in_app=self.in_app
        )
        self.assertTrue(purchase)

    def test_new_data_save_false(self):
        purchase = Purchase.parser(
            self.receipt,
            self.response,
            in_app=self.in_app,
            is_save=False
        )
        self.assertTrue(purchase)

    def test_str(self):
        purchase = Purchase.parser(
            self.receipt,
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(str(purchase),
                         'Purchase: ' + str(purchase.transaction_id))

    def test_repr(self):
        purchase = Purchase.parser(
            self.receipt,
            self.response,
            in_app=self.in_app
        )
        self.assertEqual(repr(purchase),
                         '{} <ID: {}>: "{}"'.format(purchase.product_id, purchase.id, purchase.__class__.__name__))
