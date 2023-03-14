#!/usr/bin/env bash

# Collect static files.
python manage.py collectstatic --noinput --clear
# Start server.
gunicorn -b 0.0.0.0:8000 --access-logfile /app/log.txt review.wsgi:application