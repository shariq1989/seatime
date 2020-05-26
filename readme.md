# Path to project on Pi
	cd ~/Documents/Development/SeaTime/seatime/        
# Activate venv
	source /bin/activate

# Start Django
## Forward port 8000 to local machine
	ssh -L 8000:localhost:8000 pi@192.168.0.135
	python manage.py migrate
	cd ~/Documents/Development/SeaTime/django/seatime_app && python manage.py runserver 0.0.0.0:8000
## View on local machine
	localhost:8000

# Start Vue
## Forward port 8080 to local machine
	ssh -L 8080:localhost:8080 pi@192.168.0.135
	cd ~/Documents/Development/SeaTime/django/frontend && npm run serve
## View on local machine
	localhost:8080
# Tunneling
	ssh -L 80:localhost:80 192.168.0.135
# Django Misc
	python manage.py makemigrations
	python manage.py migrate
# Django Testing
	python manage.py test seatime
# Add Python dependencies to requirements.txt
	pip freeze > requirements.txt
# Install Python dependencies
	pip install -r requirements.txt
# Building
	cd ~/home
	mkdir development
	cd development

	sudo apt install git
	git clone https://github.com/shariq1989/seatime.git

