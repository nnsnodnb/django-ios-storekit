from unittest import TestCase
from storekit.appstore import AppStoreValidator
from storekit.errors import AppValidationError
from storekit.tests.compatibility import mock

import json
import os.path


JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'response.json')


class AppStoreTest(TestCase):

    def setUp(self):
        with open(JSON_FILE_PATH, 'r') as f:
            self.response = json.loads(f.read())
        self.bundle_id = 'com.example.test'

    def tearDown(self):
        self.response = None
        self.bundle_id = None

    def test_use_sandbox(self):
        validator = AppStoreValidator(self.bundle_id, True)
        self.assertEqual(validator.url, 'https://sandbox.itunes.apple.com/verifyReceipt')

    def test_not_use_sandbox(self):
        validator = AppStoreValidator(self.bundle_id, False)
        self.assertEqual(validator.url, 'https://buy.itunes.apple.com/verifyReceipt')

    def test_use_password(self):
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            self.assertTrue(AppStoreValidator(self.bundle_id).validate('', password='test_password'))

    def test_validate_success(self):
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            self.assertTrue(AppStoreValidator(self.bundle_id).validate(''))

    def test_validate_status_error(self):
        self.response['response']['status'] = 1
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            with self.assertRaises(AppValidationError):
                _ = AppStoreValidator(self.bundle_id).validate('')

    def test_mismatch_bundle_id(self):
        self.bundle_id = 'com.example.wrong'
        with mock.patch('requests.post') as mock_post:
            mock_json = mock.Mock()
            mock_json.json.return_value = self.response
            mock_post.return_value = mock_json

            with self.assertRaises(AppValidationError):
                _ = AppStoreValidator(self.bundle_id).validate('')
