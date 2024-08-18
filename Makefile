.PHONY: clean clean-test clean-pyc clean-build build help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

docker-restart: ## restart containers
	docker compose down
	docker compose up --build -d

docker-test: docker-restart ## restart containers & test
	pytest
	
docker-test-verbose: docker-restart ## restart containers & test
	pytest -s

requirements: ## installs all requirements
	python3 -m pip install -r requirements.txt
	python3 -m pip install -r requirements-dev.txt
	
create-env: ## create .env file
	echo "ENV=DEV" > .env
	echo "DATABASE_URL=mysql+aiomysql://root:root_bot_buster@localhost/playerdata" >> .env
	echo "POOL_RECYCLE=60" >> .env
	echo "POOL_TIMEOUT=30" >> .env

setup: create-env requirements ## create env & install requirements