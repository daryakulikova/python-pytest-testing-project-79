import pytest
import tempfile
import requests_mock
import os

from page_loader import download


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def read_rb(file_path):
    with open(file_path, 'rb') as f:
        result = f.read()
    return result


def test_create_file(tmpdir, mock_html):
    file = download("https://ru.hexlet.io/courses", tmpdir)
    assert os.path.exists(file)


def test_html_file(tmpdir, mock_html, hexlet_result_html):
    path_to_html = download("https://ru.hexlet.io/courses", tmpdir)
    assert read(path_to_html) == hexlet_result_html


def test_css_file(tmpdir, mock_html, application_css):
    download("https://ru.hexlet.io/courses", tmpdir)
    result = read_rb(os.path.join(
        tmpdir,
        "ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css",))
    assert result == application_css


def test_png_file(tmpdir, mock_html, python_png):
    download("https://ru.hexlet.io/courses", tmpdir)
    result = read_rb(os.path.join(
        tmpdir,
        "ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-python.png",))
    assert result == python_png


def test_js_file(tmpdir, mock_html, runtime_js):
    download("https://ru.hexlet.io/courses", tmpdir)
    result = read_rb(os.path.join(
        tmpdir,
        "ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js",))
    assert result == runtime_js
