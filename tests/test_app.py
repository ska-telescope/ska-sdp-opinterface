from http import HTTPStatus
from typing import Callable

import pytest

from ska_sdp_opinterface.sdp import app
from . import constants as c


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def master_check(data: str) -> bool:
    return c.MASTER_KEY in data and c.MASTER_STATE in data


def run_and_check(
    client, path: str, check: [Callable[[str], bool]] = master_check
) -> None:
    result = client.get(path)
    assert result.status_code == HTTPStatus.OK
    data = result.get_data(as_text=True)
    assert check(data)


def test_db_list(client, config):
    run_and_check(client, "/db-list")


def test_db_tree(client, config):
    run_and_check(client, "/db-tree")


def test_workflows(client, config):
    run_and_check(client, "/workflows", lambda data: "realtime" in data)


def test_create(client, config):
    run_and_check(client, "/db-create", lambda data: "Submit!" in data)

    result = client.post(
        "/db-create", data={"key": c.MASTER_KEY + "/temp", "value": "test"}
    )
    assert result.status_code == HTTPStatus.FOUND


def test_test(client, config):
    run_and_check(client, "/test", lambda data: data == "Hello, World!")
