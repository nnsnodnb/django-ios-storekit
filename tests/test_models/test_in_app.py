from storekit.models import InApp

import pytest


@pytest.mark.django_db
def test_new_data_save_true(first_in_app):
    in_app = InApp.parser(first_in_app)

    assert in_app is not None


def test_new_data_save_false(first_in_app):
    in_app = InApp.parser(first_in_app, is_save=False)

    assert in_app is not None


@pytest.mark.django_db
def test_str(first_in_app):
    in_app = InApp.parser(first_in_app)

    assert str(in_app) == '{}: {}'.format(in_app.product_id, in_app.quantity)


@pytest.mark.django_db
def test_repr(first_in_app):
    in_app = InApp.parser(first_in_app)

    assert repr(in_app) == '{} <ID: {}>: "{}"'.format(in_app.product_id, in_app.id, in_app.__class__.__name__)
