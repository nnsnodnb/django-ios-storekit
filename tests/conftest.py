import json

import pytest

from .testing import JSON_FILE_PATH


@pytest.fixture(scope="class")
def read_json():
    with open(JSON_FILE_PATH, "r") as f:
        return json.loads(f.read())


@pytest.fixture(scope="class")
def bundle_id():
    return "com.example.test"
