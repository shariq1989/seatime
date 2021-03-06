#!/bin/bash
echo "activating python env"
source /home/development/seatime/seatime_env/bin/activate

echo "pull latest changes"
git -C /home/development/seatime pull

echo "install requirements"
pip3 install -r /home/development/seatime/requirements.txt

echo "make migrations"
python3 /home/development/seatime/django/seatime_app/manage.py makemigrations
echo "migrate changes"
python3 /home/development/seatime/django/seatime_app/manage.py migrate

echo "collect static files"
python3 /home/development/seatime/django/seatime_app/manage.py collectstatic

sudo systemctl restart gunicorn
