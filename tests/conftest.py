import pytest

from ska_sdp_opinterface import model
from . import constants as c


@pytest.fixture
def config():
    for txn in model.cfg.txn():
        txn.create_master({"state": c.MASTER_STATE})
    yield
    model.cfg.backend.delete(c.MASTER_KEY, must_exist=False, recursive=True)
