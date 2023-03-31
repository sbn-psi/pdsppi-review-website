#!/usr/bin/env bash
echo "start gunicorn"
/usr/local/bin/gunicorn -b 0.0.0.0:8000 --access-logfile /app/log.txt review.wsgi:application