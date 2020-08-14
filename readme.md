# Building
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
	
	bash seatime/scripts/production/createEnv.sh
	
	export DJANGO_SECRET_KEY="1c*3djyuzul-oyp%3*+8z%(n^+(#nk+cs+)d6#9u+74l%#_&ev"	
	export DJANGO_SETTINGS_MODULE="seatime_app.settings.production"
	export DJANGO_SERVER_IP="96.126.97.44"
	
# Vue - Set up remote server
	cd /var/www/html
	mkdir vue
	cd vue

	ssh-keygen (enter through values)
	copy contents of ~/.ssh/id_rsa.pub to github settings ssh page

	sudo apt install git	
	git clone git@github.com:shariq1989/seatime.git	

	cd seatime
	cd bin/ && source activate
	cd ..
	pip3 install -r requirements.txt

	cd django/frontend
	sudo apt install nodejs npm
	npm install
	npm run build
	
# Building
	cd /var/www/html/vue/seatime/django/frontend
	npm run build
	sudo service nginx restart

# Django - Set up remote server
	sudo apt update && sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
	mkdir ~/../home/development
	cd ~/../home/development
	sudo apt-get update && sudo apt-get upgrade
	sudo apt-get install git
	ssh-keygen -t rsa -b 4096
	cat /root/.ssh/id_rsa.pub
	// copy public key to github settings for shariq1989
	git clone git@github.com:shariq1989/seatime.git
	
	sudo apt-get install python3-pip
	cd seatime
	source bin/activate
	pip3 install -r requirements.txt
	export DJANGO_SECRET_KEY="1c*3djyuzul-oyp%3*+8z%(n^+(#nk+cs+)d6#9u+74l%#_&ev"	
	export DJANGO_SETTINGS_MODULE="seatime_app.settings.production"
	// insert server_ip here
	export DJANGO_SERVER_IP="96.126.97.44"
	
	cd django/seatime_app
	python3 manage.py makemigrations
	// if a one off default is needed. Use 1 and then ''.
	python3 manage.py migrate
	python3 manage.py createsuperuser
	python3 manage.py collectstatic
	
	sudo apt-get install ufw
	sudo ufw allow 8000
	
	python3 manage.py runserver 0.0.0.0:8000
	// accessible at http://<SERVER_IP>:8000/
	// admin accessible at /control
	ctrl+c
	
	gunicorn --bind 0.0.0.0:8000 seatime_app.wsgi
	ctrl+c
	deactivate
	
	sudo vi /etc/systemd/system/gunicorn.socket
	// add the following
		[Unit]
		Description=gunicorn socket

		[Socket]
		ListenStream=/run/gunicorn.sock

		[Install]
		WantedBy=sockets.target
	
	sudo vi /etc/systemd/system/gunicorn.service
	// add the following
		[Unit]
		Description=gunicorn daemon
		Requires=gunicorn.socket
		After=network.target

		sudo nano /etc/systemd/system/gunicorn.service
		// add the following
		/etc/systemd/system/gunicorn.service

		[Unit]
		Description=gunicorn daemon
		Requires=gunicorn.socket
		After=network.target

		[Service]
		User=root
		Group=www-data
		WorkingDirectory=/home/development/seatime/django/seatime_app
		ExecStart=/usr/local/bin/gunicorn \
			  --access-logfile - \
			  --workers 3 \
			  --bind unix:/run/gunicorn.sock \
			  seatime_app.wsgi:application

		[Install]
		WantedBy=multi-user.target

	sudo systemctl start gunicorn.socket
	sudo systemctl enable gunicorn.socket
	// verify that gunicorn started correctly
	sudo systemctl status gunicorn.socket
	// verify that sock exists
	file /run/gunicorn.sock
	// if errors
		// change gunicorn.service file
		// sudo systemctl daemon-reload
    		// sudo systemctl restart gunicorn
		// sudo journalctl -u gunicorn
	
	sudo apt-get install nginx
	sudo vi /etc/nginx/sites-available/seatime
	// add the following lines
		server {
		    listen 80;
		    server_name 96.126.97.44;

		    location = /favicon.ico { access_log off; log_not_found off; }
		    location /staticfiles/ {
			root /home/development/seatime/django/seatime_app/seatime_app;
		    }

		    location / {
			include proxy_params;
			proxy_pass http://unix:/run/gunicorn.sock;
		    }
		}
	
	sudo ln -s /etc/nginx/sites-available/seatime /etc/nginx/sites-enabled	
	sudo nginx -t
	sudo systemctl restart nginx
	sudo ufw delete allow 8000
	sudo ufw allow 'Nginx Full'
	
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
