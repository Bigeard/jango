# Jango (Fett) 
***Robin Bigeard***

  ![XML page](/img/screenshot-1.png "screenshot-1")
  ![Orders page](/img/screenshot-2.png "screenshot-2")
  ![API page](/img/screenshot-3.png "screenshot-3")
  ![Admin page](/img/screenshot-4.png "screenshot-4")

## Install Python3, Pip3 :

```bash
python3 -V
// Python 3.7.3
```
```bash
pip3 -V
// pip 19.0.3 from /usr/lib/python3.7/site-packages/pip (python 3.7)
```

## Virtuel Environment
```bash
pip3 install virtualenv
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

## Install Django 

```bash
pip install django
// Python 3.7.3
```

```bash
python -m django --version
// 2.2
```

## Create project Django

Create project.
```bash
django-admin startproject jango
```

See all command.
```bash
cd jango
python manage.py
```

Run server.
```bash
python manage.py runserver
```

Create app.
```bash
python manage.py startapp orders
```

## Heroku

### Install Heroku

First install client heroku servives.
https://www.heroku.com/


```bash
pip install gunicorn
```

add file `Procfile`.
```
web: gunicorn jango.wsgi --log-file -
```

Install dj-database-url for connection to postgres directly by URL.
```bash
pip install dj-database-url
```

Install psycopg2
```bash
pip install psycopg2
```

Install whitenoise
```bash
pip install whitenoise
```

Create file requierements.txt for heroku,
it references all pip installations.
```bash
pip freeze > requirements.txt
```

### Comamnd Heroku

```bash
heroku run python manage.py migrate
```

```bash
heroku run bash -a app-jango
```

```bash
`$ server-heroku :` python manage.py migrate
```

```bash
`$ server-heroku :` python manage.py createsuperuser 
```

## Database Command
```
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username=bigeard --email=robin.bigeard@gmail.com
```

## Source 

https://docs.djangoproject.com/en/2.2/

https://www.geeksforgeeks.org/xml-parsing-python/
https://python-django.dev/page-xml-python-xpath

https://www.youtube.com/watch?v=263xt_4mBNc
https://www.youtube.com/watch?v=eJ0sEUB3d1U
https://www.youtube.com/watch?v=D6esTdOLXh4

https://devcenter.heroku.com/articles/getting-started-with-python