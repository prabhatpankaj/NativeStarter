.PHONY: install migrate clear

install:
	pip install --upgrade setuptools pip
	pip install -r requirements.txt

migrate:
	python src/manage.py makemigrations
	python src/manage.py migrate

clear:
	rm -rf media_cdn/*
	rm -rf media_cdn/*
	rm -rf src/db.sqlite3
	
run:
	python src/manage.py runserver 0.0.0.0:8080
