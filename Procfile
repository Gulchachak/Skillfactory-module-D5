release: python manage.py migrate
release: python manage.py loaddata data.xml
web: gunicorn my_site.wsgi
