from storekit.models import Receipt

import pytest


@pytest.mark.django_db
def test_new_data_save_true(read_json, first_in_app):
    receipt = Receipt.parser(read_json["receipt"], in_app=first_in_app)

    assert receipt is not None


@pytest.mark.django_db
def test_new_data_save_false(read_json, first_in_app):
    receipt = Receipt.parser(read_json["receipt"], in_app=first_in_app, is_save=False)

    assert receipt is not None


@pytest.mark.django_db
def test_str(read_json, first_in_app):
    receipt = Receipt.parser(read_json["receipt"], in_app=first_in_app)

    assert str(receipt) == "[{}] {}: {}".format(receipt.receipt_type, receipt.bundle_id, receipt.application_version)


@pytest.mark.django_db
def test_repr(read_json, first_in_app):
    receipt = Receipt.parser(read_json["receipt"], in_app=first_in_app)

    assert repr(receipt) == '<ID: {}>: "{}"'.format(receipt.id, receipt.__class__.__name__)
