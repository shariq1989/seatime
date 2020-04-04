#!/bin/bash
echo "activating python env"
cd ~/Documents/Development/SeaTime/bin/ && source activate
echo "pulling latest code"
git pull
echo "starting django webservice"
cd ~/Documents/Development/SeaTime/django/seatime_app && python manage.py runserver 0.0.0.0:8000
