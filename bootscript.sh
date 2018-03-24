#!/bin/bash
source /home/martin/ledky/backend/venv/bin/activate
fuser -k 8080/tcp  # will kill the app if it's already running
FLASK_APP=/home/martin/ledky/backend/app.py nohup flask run --host=0.0.0.0 --port=8080 > /home/martin/ledky/backend/logs/stdout.log 2>/home/martin/ledky/backend/logs/stderr.log &
