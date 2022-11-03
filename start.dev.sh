#!/usr/bin/env bash

# Collect static files.
python manage.py collectstatic --noinput --clear
# Start server.
python manage.py runserver 0.0.0.0:8000 --settings=review.settings.dev