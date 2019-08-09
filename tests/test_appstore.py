from storekit.appstore import AppStoreValidator
from storekit.errors import AppValidationError

import copy
import pytest


def test_use_sandbox(bundle_id):
    validator = AppStoreValidator(bundle_id, True)

    assert validator.url == 'https://sandbox.itunes.apple.com/verifyReceipt'


def test_not_use(bundle_id):
    validator = AppStoreValidator(bundle_id, False)

    assert validator.url == 'https://buy.itunes.apple.com/verifyReceipt'


@pytest.mark.django_db
def test_use_password(read_json, bundle_id, requests_mock):
    validator = AppStoreValidator(bundle_id)
    requests_mock.post(validator.url, json=read_json)
    result = validator.validate('', password='test_password')

    assert result


@pytest.mark.django_db
def test_validate_success(read_json, bundle_id, requests_mock):
    validator = AppStoreValidator(bundle_id)
    requests_mock.post(validator.url, json=read_json)
    result = validator.validate('')

    assert result


def test_validate_status_error(read_json, bundle_id, requests_mock):
    validator = AppStoreValidator(bundle_id)
    json_data = copy.copy(read_json)
    json_data['status'] = 1
    requests_mock.post(validator.url, json=json_data)

    with pytest.raises(AppValidationError):
        _ = validator.validate('')


def test_mismatch_bundle_id(read_json, requests_mock):
    validator = AppStoreValidator('com.example.wrong')
    requests_mock.post(validator.url, json=read_json)

    with pytest.raises(AppValidationError):
        _ = validator.validate('')
