#!make
PROJECT_VERSION := 0.3.2

SHELL := /bin/bash

.PHONY: help build jupyter tag


.DEFAULT: help

help:
	@echo "make build"
	@echo "       Build the docker image."
	@echo "make jupyter"
	@echo "       Start the Jupyter server."
	@echo "make tag"
	@echo "       Make a tag on Github."


build:
	docker-compose build jupyter

jupyter: build
	@echo "http://localhost:8888"
	docker-compose up jupyter

tag:
	git tag -a ${PROJECT_VERSION} -m "new tag"
	git push --tags
