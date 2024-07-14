#!/bin/sh

WORKERS=$(expr $(nproc) \* 2 + 1)

echo "Starting app with ${WORKERS} workers."
exec gunicorn --bind 0.0.0.0:80 --workers $WORKERS --access-logfile - --error-logfile - src.main:app
