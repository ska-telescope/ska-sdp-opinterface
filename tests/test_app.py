from http import HTTPStatus
import pytest

from ska_sdp_opinterface.sdp import app
from . import constants as c


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def run_and_check(client, path: str):
    rv = client.get("/db_list")
    assert rv.status_code == HTTPStatus.OK
    data = rv.get_data(as_text=True)
    assert c.MASTER_KEY in data and c.MASTER_STATE in data


def test_db_list(client, config):
    run_and_check(client, "/db_list")


def test_db_tree(client, config):
    run_and_check(client, "/db_tree")


def test_workflows(client, config):
    run_and_check(client, "/workflows")


def test_create(client, config):
    rv = client.post(
        "/db_create", data={"key": c.MASTER_KEY + "/temp", "value": "test"}
    )
    assert rv.status_code == HTTPStatus.FOUND
