install:
	poetry install
migrate:
	poetry run python vidago/manage.py migrate

migrations:
	poetry run python vidago/manage.py makemigrations

run-server:
	poetry run python vidago/manage.py runserver

superuser:
	poetry run python vidago/manage.py createsuperuser

update: install migrate;