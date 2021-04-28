SHELL := /bin/bash

manage_py := docker exec -it backend python3 app/manage.py

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

gunicorn:
	gunicorn booksharing.wsgi --workers=4 --chdir=/home/kostiantyn/PycharmProjects/booksharing/app --max-requests=10000

uwsgi:
	 uwsgi --http :8001 --chdir=/home/kostiantyn/PycharmProjects/booksharing/app --module booksharing.wsgi --master --processes 4 --threads 2

collectstatic:
	$(manage_py) collectstatic --noinput && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static web:/etc/nginx/static

tests:
	pytest app/

tests_coverage:
	pytest app/ --cov=app --cov-report html

build-dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

build: build-dev collectstatic

build_down:
	docker-compose down

check_docker_image_memory: # Проверить сколько места заняли образы
	docker system df

clear_docker_memory: # Очистить память от образов
	docker system prune -a

docker_backend:
	docker exect -it backend bash