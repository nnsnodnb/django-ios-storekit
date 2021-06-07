from storekit.models import Response

import pytest


@pytest.mark.django_db
def test_new_data_save_true(read_json, first_in_app):
    response = Response.parser(read_json, in_app=first_in_app)

    assert response is not None


@pytest.mark.django_db
def test_new_data_save_false(read_json, first_in_app):
    response = Response.parser(read_json, in_app=first_in_app, is_save=False)

    assert response is not None


@pytest.mark.django_db
def test_str(read_json, first_in_app):
    response = Response.parser(read_json, in_app=first_in_app)

    assert str(response) == "Response: {}".format(response.environment)


@pytest.mark.django_db
def test_repr(read_json, first_in_app):
    response = Response.parser(read_json, in_app=first_in_app)

    assert repr(response) == '<ID: {}>: "{}"'.format(response.id, response.__class__.__name__)
