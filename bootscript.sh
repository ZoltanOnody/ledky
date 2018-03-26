#!/bin/bash
WORKDIR=/home/martin/ledky/

source "$WORKDIR"backend/venv/bin/activate
fuser -k 8080/tcp  # will kill the app if it's already running
FLASK_APP="$WORKDIR"backend/app.py nohup flask run --host=0.0.0.0 --port=8080 > "$WORKDIR"backend/logs/stdout.log 2>"$WORKDIR"backend/logs/stderr.log &
