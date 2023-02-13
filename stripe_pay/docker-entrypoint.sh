#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations orders
python manage.py migrate

echo "Load fixtures"
python manage.py loaddata fixtures.json

echo "Starting server"
gunicorn stripe_pay.wsgi:application --bind 0:8000