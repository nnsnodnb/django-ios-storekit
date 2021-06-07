import pytest


@pytest.fixture(scope="function")
def first_in_app(read_json):
    return read_json["receipt"]["in_app"][0]
