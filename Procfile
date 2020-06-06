release: python manage.py migrate
web: gunicorn --pythonpath django/seatime_app seatime_app.wsgi