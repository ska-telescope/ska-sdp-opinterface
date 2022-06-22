""" Pytest setup file for the SDP Operator interface"""

import pytest

from ska_sdp_opinterface import model

from . import constants as c


@pytest.fixture
def config():
    """Create test entry and delete again on teardown"""
    backend = model.cfg.backend
    for txn in model.cfg.txn():
        txn.create_controller({"state": c.CONTROLLER_STATE})
    backend.create(c.SCRIPT_KEY, c.SCRIPT_VALUE)
    yield
    for key in (c.CONTROLLER_KEY, c.SCRIPT_KEY):
        backend.delete(key, must_exist=False, recursive=True)
