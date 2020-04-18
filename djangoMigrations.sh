#!/bin/bash
echo "activating python env"
cd ~/Documents/Development/SeaTime/bin/ && source activate
echo "make migrations"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py makemigrations
echo "starting django webservice"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py migrate
