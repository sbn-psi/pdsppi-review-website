#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
	  echo 'sleep...'
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$DEBUG" = 'True' ]
then
    python manage.py makemigrations --settings=review.settings.dev
    python manage.py migrate --settings=review.settings.dev
else
    python manage.py makemigrations --settings=review.settings.production
    python manage.py migrate --settings=review.settings.production
fi

echo "PostgreSQL migrations completed"

exec "$@"