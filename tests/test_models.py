from storekit.models import InApp, Receipt, Response

import pytest

"""
@pytest.fixture(scope='function')
def first_in_app(read_json):
    return read_json['receipt']['in_app'][0]


@pytest.mark.usefixtures('first_in_app')
class TestInApp(object):

    def test_new_data_save_true(self):
        in_app = InApp.parser(self.first_in_app)
        assert in_app is not None

    def test_new_data_save_false(self):
        in_app = InApp.parser(self.first_in_app, is_save=False)

        assert in_app is not None

    def test_str(self):
        in_app = InApp.parser(self.first_in_app)

        assert str(in_app), f'{self.first_in_app.product_id}: {self.first_in_app.quantity}'

    def test_repr(self):
        in_app = InApp.parser(self.first_in_app)

        assert repr(in_app), f'{in_app.product_id} <ID: {in_app.id}>: "{in_app.__class__.__name__}"'


@pytest.mark.usefixtures('read_json', 'first_in_app')
class TestReceipt(object):

    def test_new_data_save_true(self):
        receipt = Receipt.parser(self.read_json['receipt'], in_app=self.first_in_app)

        assert receipt is not None

    def test_new_data_save_false(self):
        receipt = Receipt.parser(self.read_json['receipt'], in_app=self.first_in_app, is_save=False)

        assert receipt is not None

    def test_str(self):
        receipt = Receipt.parser(self.read_json['receipt'], in_app=self.first_in_app)

        assert str(receipt), f'[{receipt.receipt_type}] {receipt.bundle_id}: {receipt.application_version}'

    def test_repr(self):
        receipt = Receipt.parser(self.read_json['receipt'], in_app=self.first_in_app)

        assert repr(receipt), f'<ID: {receipt.id}>: "{receipt.__class__.__name__}"'


@pytest.mark.usefixtures('read_json', 'first_in_app')
class TestResponse(object):

    def test_new_data_save_true(self):
        response = Response.parser(self.read_json, in_app=self.first_in_app)

        assert response is not None

    def test_new_data_save_false(self):
        response = Response.parser(self.read_json, in_app=self.first_in_app, is_save=False)

        assert response is not None

    def test_str(self):
        response = Response.parser(self.read_json, in_app=self.first_in_app)

        assert str(response), f'Response: {response.environment}'

    def test_repr(self):
        response = Response.parser(self.read_json, in_app=self.in_app)

        assert repr(response), f'<ID: {response.id}>: "{response.__class__.__name__}"'
"""
