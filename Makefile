# Makefile

install: # выполнить установку зависимостей
	poetry lock ;\
	poetry install


build: # собрать пакет
	poetry build


package-install: # установка пакета из ОС (запускать из корня проекта)
	uv tool install --reinstall --force dist/*.whl


lint: # запуск линтера (flake8)
	poetry run flake8 page_loader ;\
	poetry run flake8 tests

test-cov:
	poetry run pytest --cov=page_loader -vv --cov-report xml

test: # запуск pytest
	poetry run pytest -vv

.PHONY: install build publish package-install lint test test-cov