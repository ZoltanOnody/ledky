# Deployment

```
source venv/bin/activate
fuser -k 8080/tcp  # will kill the app if it's already running
FLASK_APP=app.py nohup flask run --host=0.0.0.0 --port=8080 > logs/stdout.log 2>logs/stderr.log &
```
