"""
This module contains the "model" layer.

This includes configuration database interactions and building data structures
for display.
"""
import json
import sys
from typing import Dict, List

import ska_sdp_config

DELIMITER = ":"
cfg = ska_sdp_config.Config(backend="memory" if "pytest" in sys.modules else "etcd3")


def get_raw_dict(as_text: bool = True) -> Dict:
    entries = {}
    for txn in cfg.txn():
        for key in txn.raw.list_keys('/', recurse=8):
            value = txn.raw.get(key)
            if not as_text:
                value = json.loads(value)
            entries[key] = value
    return entries


def _combine_key(parent: str, key: str) -> str:
    return DELIMITER.join((parent, key))


def _clean_key(key: str) -> str:
    k = key[1:] if key.startswith("/") else key
    return k.replace("/", DELIMITER)


def _to_node(key: str, parent: str, text: str) -> Dict:
    return {"id": _clean_key(key), "parent": _clean_key(parent), "text": text}


def _add_dict(data: List, d: Dict, parent: str = "#") -> None:
    for key, value in d.items():

        # Combine the parent and key to avoid name clashes.
        text = key
        k = key if parent == "#" else _combine_key(parent, key)

        if isinstance(value, dict):
            _add_dict(data, value, parent=k)
        else:
            text += ": "+str(value)

        data.append(_to_node(k, parent, text))


def get_tree_data() -> List:
    data = []
    _add_dict(data, get_raw_dict(as_text=False))
    return data


def get_workflows() -> List:
    data = [_to_node(key, "#", key) for key in ("batch", "realtime")]

    types = {"batch": [], "realtime": []}
    for txn in cfg.txn():
        for key in txn.raw.list_keys('/workflow', recurse=3):
            value = txn.raw.get(key)
            _, _, k = key.split('/')
            wf_type, name, version = k.split(":")
            if name not in types[wf_type]:
                data.append(_to_node(name, wf_type, name))
                types[wf_type].append(name)
            k = _combine_key(name, version)
            data.append(_to_node(k, name, version))
            _add_dict(data, json.loads(value), k)
    return data


def create_entry(key: str, value: str) -> None:
    for txn in cfg.txn():
        txn.raw.create(key, value)
    print(key + ",  " + value)
