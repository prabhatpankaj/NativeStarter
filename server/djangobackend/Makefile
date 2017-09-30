.PHONY: install migrate run
install:
	pip install --upgrade setuptools pip
	pip install -r requirements.txt

migrate:
	python src/manage.py makemigrations
	python src/manage.py migrate

clear:
	rm -rf media_cdn/cache
	rm -rf media_cdn/images
	
auth:
	python src/manage.py loaddata fixtures/auth.user.json

run:
	python src/manage.py runserver 0.0.0.0:8080
