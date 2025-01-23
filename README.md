[![Maintainability](https://api.codeclimate.com/v1/badges/ffde038caa8de333501d/maintainability)](https://codeclimate.com/github/daryakulikova/python-pytest-testing-project-79/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ffde038caa8de333501d/test_coverage)](https://codeclimate.com/github/daryakulikova/python-pytest-testing-project-79/test_coverage)
![main workflow](https://github.com/daryakulikova/python-pytest-testing-project-79/actions/workflows/main.yml/badge.svg)

## Page loader

Данная утилита командной строки скачивает страницу и её локальные ресурсы из сети  
и кладет в указанную **существующую** директорию (по умолчанию в директорию запуска программы).  
По результату работы утилиты мы получаем html-страницу со ссылками на скачанные ресурсы.
```bash
usage: page-loader [-h] [-out OUTPUT] url_to_download

Page loader

positional arguments:
  url_to_download

optional arguments:
  -h, --help            show this help message and exit
  -out OUTPUT, --output OUTPUT
                        set path to the existing directory (current directory by default)
```

##### Пример работы пакета:
[![asciicast](https://asciinema.org/a/8gRAhNb6cEBdHBPMyS7Pr3wbf.svg)](https://asciinema.org/a/8gRAhNb6cEBdHBPMyS7Pr3wbf)

##### Для установки зависимостей используйте
```bash
$ make install
```
