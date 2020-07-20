#!/bin/bash
echo "activating python env"
cd ~/Documents/Development/SeaTime/bin/ && source activate
echo "pulling latest code"
git pull

heroku pg:psql postgresql-contoured-81635 --app seatime-django --command "DELETE FROM seatime_staffposition;"
heroku pg:psql postgresql-contoured-81635 --app seatime-django --command "DELETE FROM seatime_rating;"

cd ~/Documents/Development/SeaTime/django/seatime_app || exit
python3 manage.py loaddata seatime/fixtures/initial_data.json
