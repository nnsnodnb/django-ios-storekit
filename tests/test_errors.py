from storekit.errors import AppValidationError


def test_app_validation_error():
    error = AppValidationError(msg='')
    error.response = {'status': 1}

    assert error.response is not None
