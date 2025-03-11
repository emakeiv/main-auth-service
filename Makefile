.PHONY: install
install :
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: format
format :
	black src/*.py src/*/*.py src/*/*/*.py tst/*.py

.PHONY: lint
lint:
	pylint --disable=R,C src/*/*.py src/*/*/*.py

.PHONY: test
test:
	pytest -vv --cov=app tst/*

.PHONY: build
build:
	docker build -t main-auth-service .
	# $(eval DOCKER_IMAGE_ID := $(shell docker images -q main-auth-service))

.PHONY: run
run:
	docker run -p 127.0.0.1:8000:8000 main-auth-service

.PHONY: deploy
deploy:
	# deploy

.PHONY: all
all: 
	install format lint test build deploy