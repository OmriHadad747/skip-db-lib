import pytest
import flask
import flask.testing

from typing import Any, Dict
from skip_db_lib import create_app
from skip_db_lib import config


@pytest.fixture(scope="session")
def app() -> flask.Flask:
    """
    app fixture for unit testing
    including mocked database operations

    Yields:
        Iterator[flask.Flask]: flask's application instance
    """
    app = create_app(config.TestConfig)

    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def test_id() -> str:
    return "63777f6473beddcaff67686c"

@pytest.fixture(scope="session")
def test_customer() -> Dict[str, Any]:
    return {
        "_id": {
            "$oid": "63777f6473beddcaff67686c"
        },
        "created_at": {
            "$date": "2022-11-18T14:49:40.812Z"
        },
        "password": "pbkdf2:sha256:260000$dTmnjaEGJ8NSFyws$c3d3149d6b1e43b2d368d25dfd7df7223214878ea26255bbcadb4dda01db9faf",
        "email": "c1@gmail.com",
        "phone": "111",
        "address": "address 1",
        "county": "county 1",
        "rating": 1,
        "job_history": [],
        "location": [
            -73.9667,
            40.74
        ],
        "registration_token": "1"
    }