APP_NAME=main-auth-service
COMPOSE_FILE=.docker/docker-compose.yaml
DOCKER_IMAGE=main-auth-service
DOCKER_HUB_USER=emakeiv
TAG=latest
FULL_IMAGE_NAME := $(DOCKER_HUB_USER)/$(DOCKER_IMAGE):$(TAG)

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
	docker build -t ${DOCKER_IMAGE} -f .docker/app/dockerfile .
	# $(eval DOCKER_IMAGE_ID := $(shell docker images -q main-auth-service))

.PHONY: push
push:
	docker push $(FULL_IMAGE_NAME)
	

.PHONY: run
run:
	docker run -p 127.0.0.1:5000:5000 main-auth-service

.PHONY: deploy
deploy:
	# deploy

.PHONY: all
all: 
	install format lint test build deploy