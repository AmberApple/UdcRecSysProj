#!/bin/sh

#python manage.py flush --no-input
#python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser
#python manage.py collectstatic

exec "$@"