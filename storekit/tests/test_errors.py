from unittest import TestCase
from storekit.errors import AppValidationError


class ErrorsTest(TestCase):

    def setUp(self):
        self.error = AppValidationError(msg='')

    def tearDown(self):
        self.error = None

    def test_app_validation_error(self):
        self.error.response = {'status': 1}
        self.assertNotEqual(self.error.response, None)
