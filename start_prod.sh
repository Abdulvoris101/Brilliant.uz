python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate
nohup python manage.py run &
gunicorn --workers=1 --worker-class=gthread --log-level error --timeout=30 --threads=4 server.wsgi -b 0.0.0.0:8001 
