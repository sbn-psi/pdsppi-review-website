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

python manage.py makemigrations --settings=review.settings.vger
python manage.py migrate --settings=review.settings.vger

echo "PostgreSQL migrations completed"

exec "$@"