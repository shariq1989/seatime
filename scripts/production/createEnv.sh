#!/bin/bash
# TODO
# cd ~/home || exit
# mkdir development
# sudo apt install git
# git clone git@github.com:shariq1989/seatime.git

echo "activating python env"
cd /home/development/seatime/bin/ && source activate
cd ..
echo "install pip3"
sudo apt install python3-pip
alias python=python3
alias pip=pip3

echo "install requirements"
pip3 install -r requirements.txt

echo "make migrations"
python3 /home/development/seatime/django/seatime_app/manage.py makemigrations
echo "migrate changes"
python3 /home/development/seatime/django/seatime_app/manage.py migrate
python3 /home/development/seatime/django/seatime_app/manage.py createsuperuser
python3 /home/development/seatime/django/seatime_app/manage.py collectstatic
