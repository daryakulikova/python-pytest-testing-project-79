import os
import pytest
import asyncio
import pytest_asyncio
import requests_mock

FIXTURES_FOLDER = 'fixtures'


@pytest.fixture(scope='module')
def hexlet_html():
    path = os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'hexlet.html')
    with open(path, "r") as f:
        return f.read()


@pytest.fixture(scope='module')
def application_css():
    path = os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'application.css')
    with open(path, "rb") as f:
        return f.read()


@pytest.fixture(scope='module')
def python_png():
    path = os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'python.png')
    with open(path, "rb") as f:
        return f.read()


@pytest.fixture(scope='module')
def runtime_js():
    path = os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'runtime.js')
    with open(path, "rb") as f:
        return f.read()


@pytest.fixture(scope='module')
def hexlet_result_html():
    path = os.path.join(os.path.dirname(__file__),
                        FIXTURES_FOLDER, 'hexlet_result.html')
    with open(path, "r") as f:
        return f.read()


@pytest.fixture(scope='module')
def mock_html(hexlet_html, application_css, python_png, runtime_js):
    with requests_mock.Mocker() as m:
        m.get(
            "https://ru.hexlet.io/courses",
            text=hexlet_html,
        )
        m.get(
            "/assets/application.css",
            content=application_css,
        )
        m.get(
            "/assets/professions/python.png",
            content=python_png,
        )
        m.get(
            "https://ru.hexlet.io/packs/js/runtime.js",
            content=runtime_js,
        )
        yield m
