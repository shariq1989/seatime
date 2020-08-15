# Building Django
	# Remove from known_hosts on local machine
	# Copy local id_rsa.pub
	# Log into remote server
	ssh-keygen
	# Enter through until key is created
	vi .ssh/authorized_keys
	# Paste key here
	
	cat ~/.ssh/id_rsa.pub
	# Paste in Github->Settings->SSH keys
	mkdir /home/development
	sudo apt install git
	cd /home/development
	git clone git@github.com:shariq1989/seatime.git
		
	export DJANGO_SECRET_KEY="1c*3djyuzul-oyp%3*+8z%(n^+(#nk+cs+)d6#9u+74l%#_&ev"	
	export DJANGO_SETTINGS_MODULE="seatime_app.settings.production"
	export DJANGO_SERVER_IP="96.126.97.44"
	
	bash /home/development/seatime/scripts/production/createEnv.sh
	
	file /run/gunicorn.sock
	sudo journalctl -u gunicorn.socket
	sudo systemctl status gunicorn
	curl --unix-socket /run/gunicorn.sock localhost
	sudo systemctl status gunicorn

# Django - Making Changes
### If you update your Django application, you can restart the Gunicorn process to pick up the changes by typing:

    sudo systemctl restart gunicorn

### If you change Gunicorn socket or service files, reload the daemon and restart the process by typing:

    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn.socket gunicorn.service

### If you change the Nginx server block configuration, test the configuration and then Nginx by typing:

    sudo nginx -t && sudo systemctl restart nginx


# Vue - Set up remote server
	cd /var/www/html
	mkdir vue
	cd vue

	cd django/frontend
	sudo apt install nodejs npm
	npm install
	npm run build
	
	cd /var/www/html/vue/seatime/django/frontend
	npm run build
	sudo service nginx restart

# Building
	cd /var/www/html/vue/seatime/django/frontend
	npm run build
	sudo service nginx restart

# Misc. Operations
#### Tunneling
	ssh -L 80:localhost:80 192.168.0.135
#### Django Testing
	python manage.py test seatime
#### Add Python dependencies to requirements.txt
	pip freeze > requirements.txt	
## DB Ops
#### Dump DB to console 
    python3 manage.py dumpdata seatime
#### Load fixture
    python3 manage.py loaddata initial_data.json
#### Log into heroku managed DB
    heroku pg:psql postgresql-contoured-81635 --app seatime-django
