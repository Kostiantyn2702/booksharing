SHELL := /bin/bash

manage_py := python app/manage.py

runserver:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell_plus:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake8:
	flake8 app/

celery:
	celery -A booksharing worker -l info #TODO

freeze:
	pip freeze > requirements.txt
