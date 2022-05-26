""" Tests of the data model from the SDP operator interface"""

from ska_sdp_opinterface import model

from . import constants as c


def _test_raw_dict():
    dct = model.get_raw_dict()
    assert isinstance(dct, dict)
    assert len(dct) == 1
    assert c.CONTROLLER_STATE in dct[c.CONTROLLER_KEY]


def _test_tree_data():
    # pylint: disable=protected-access
    data = model.get_tree_data()
    assert isinstance(data, list)
    assert len(dict) == 2
    # The recursive algorithm inverts the order.
    key = c.CONTROLLER_KEY[1:]
    assert data[1]["id"] == key
    assert data[0]["id"] == model._combine_key(key, "state")


def _test_scripts():
    data = model.get_scripts()
    assert len(data) == 5
    assert data[0]["id"] == "batch"
    assert data[1]["id"] == "realtime"
