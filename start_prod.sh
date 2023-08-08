python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py migrate
nohup python manage.py run &
uwsgi --ini uwsgi.ini