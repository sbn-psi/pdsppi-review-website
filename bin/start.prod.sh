#!/usr/bin/env bash

# Start nginx server
# binds to port 80
echo "Start nginx..."
nginx

# Start gunicorn server
# binds to port 8000
echo "Start gunicorn server on port 8000..."
gunicorn -b 0.0.0.0:8000 --access-logfile /app/log.txt review.wsgi:application