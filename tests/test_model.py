from ska_sdp_opinterface import model
from . import constants as c


def test_raw_dict(config):
    d = model.get_raw_dict()
    assert isinstance(d, dict)
    assert len(d) == 1
    assert c.MASTER_STATE in d[c.MASTER_KEY]


def test_tree_data(config):
    d = model.get_tree_data()
    print(d)
    assert isinstance(d, list)
    assert len(d) == 2
    # The recursive algorithm inverts the order.
    key = c.MASTER_KEY[1:]
    assert d[1]["id"] == key
    assert d[0]["id"] == model._combine_key(key, "state")


def test_workflows(config):
    d = model.get_workflows()
    assert len(d) == 5
    assert d[0]["id"] == "batch"
    assert d[1]["id"] == "realtime"
