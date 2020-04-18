#!/bin/bash
echo "activating python env"
cd ~/Documents/Development/SeaTime/bin/ && source activate
echo "pulling latest code"
git pull
echo "make migrations"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py makemigrations
echo "migrate changes"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py migrate
echo "starting django webservice"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py runserver 0.0.0.0:8000
