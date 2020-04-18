#!/bin/bash
echo "activating python env"
source ~/Documents/Development/SeaTime/bin/activate
echo "pulling latest code"
git pull
echo "starting django webservice"
python ~/Documents/Development/SeaTime/django/seatime_app/manage.py runserver 0.0.0.0:8000
