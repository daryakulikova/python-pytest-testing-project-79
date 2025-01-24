# Makefile

install: # выполнить установку зависимостей
	poetry lock ;\
	poetry install


build: # собрать пакет
	poetry build


package-install: # установка пакета из ОС (запускать из корня проекта)
	uv tool install --reinstall dist/*.whl


lint: # запуск линтера (flake8)
	poetry run flake8 hexlet_code ;\
	poetry run flake8 tests

test-cov:
	poetry run pytest --cov=hexlet_code -vv --cov-report xml

test: # запуск pytest
	poetry run pytest -vv

.PHONY: install build publish package-install lint test test-cov