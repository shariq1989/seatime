#!/bin/bash
# TODO
# sudo apt install git
# git clone git@github.com:shariq1989/seatime.git

sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

echo "activating python env"
cd /home/development/seatime/ || exit
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
virtualenv seatime_env
source seatime_env/bin/activate
echo "install pip3"
alias python="python3"
alias pip="pip3"

echo "install requirements"
pip3 install -r requirements.txt

echo "make migrations"
python3 /home/development/seatime/django/seatime_app/manage.py makemigrations
echo "migrate changes"
python3 /home/development/seatime/django/seatime_app/manage.py migrate

# TODO
echo "create super user"
python3 /home/development/seatime/django/seatime_app/manage.py createsuperuser

echo "collect static files"
python3 /home/development/seatime/django/seatime_app/manage.py collectstatic

# firewall stuff
sudo apt install ufw
sudo ufw allow 8000

cp -a /home/development/seatime/scripts/production/gunicorn/. /etc/systemd/system/

sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn

cp -a /home/development/seatime/scripts/production/nginx/seatime /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/seatime /etc/nginx/sites-enabled
sudo systemctl restart nginx

sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
