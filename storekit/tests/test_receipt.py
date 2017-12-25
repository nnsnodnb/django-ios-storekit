from django.conf import settings
from unittest import TestCase
from storekit.errors import AppValidationError
from storekit.receipt import normal_receipt, subscribe_receipt
from storekit.tests.compatibility import mock

import json
import os.path

JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'response.json')


class NormalReceiptTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())
        self.bundle_id = settings.STOREKIT_APP_BUNDLE_ID
        self.sandbox = False

    def tearDown(self):
        self.response = None
        self.bundle_id = None
        self.sandbox = None

    def test_success(self):
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            self.assertTrue(normal_receipt(receipt='', sandbox=self.sandbox))

    def test_failure_status_code(self):
        self.response['response']['status'] = 1
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            with self.assertRaises(AppValidationError):
                normal_receipt(receipt='', sandbox=self.sandbox)


class SubscribeReceiptTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())
        self.bundle_id = settings.STOREKIT_APP_BUNDLE_ID
        self.sandbox = False

    def tearDown(self):
        self.response = None
        self.bundle_id = None
        self.sandbox = None

    def test_success(self):
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            self.assertTrue(subscribe_receipt(receipt='', sandbox=self.sandbox))

    def test_failure_status_code(self):
        self.response['response']['status'] = 1
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            with self.assertRaises(AppValidationError):
                subscribe_receipt(receipt='', sandbox=self.sandbox)
