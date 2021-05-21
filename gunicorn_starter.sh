#!/bin/sh
export PYTHONPATH=src
gunicorn ska_sdp_opinterface.sdp:app -w 2 --threads 3 -b 0.0.0.0:8000


