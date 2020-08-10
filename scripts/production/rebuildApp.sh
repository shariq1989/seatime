#!/bin/bash
echo "activating python env"
cd /home/development/seatime/bin/ && source activate

echo "pull latest changes"
git -C /home/development/seatime pull

echo "install requirements"
pip3 install -r requirements.txt

echo "make migrations"
python3 /home/development/seatime/django/seatime_app/manage.py makemigrations
echo "migrate changes"
python3 /home/development/seatime/django/seatime_app/manage.py migrate

echo "collect static files"
python3 /home/development/seatime/django/seatime_app/manage.py collectstatic

