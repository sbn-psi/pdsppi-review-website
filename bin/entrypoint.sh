#!/usr/bin/env bash

### Post-install script that runs initial migrations
#### These can also be run by hand after starting the application

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
	  echo 'sleep...'
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [[ "$DEBUG" == 'True' ]]
then
  python manage.py migrate --settings=review.settings.dev
elif [[ "$DEBUG" == 'False' ]]
then
  python manage.py migrate --settings=review.settings.production
fi

# Collect static files.
python manage.py collectstatic --noinput --clear

echo "PostgreSQL migrations completed"

exec "$@"