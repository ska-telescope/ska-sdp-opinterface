import pytest

from ska_sdp_opinterface import model
from . import constants as c


@pytest.fixture
def config():
    backend = model.cfg.backend
    for txn in model.cfg.txn():
        txn.create_master({"state": c.MASTER_STATE})
    backend.create(c.WORKFLOW_KEY, c.WORKFLOW_VALUE)
    yield
    for key in (c.MASTER_KEY, c.WORKFLOW_KEY):
        backend.delete(key, must_exist=False, recursive=True)
