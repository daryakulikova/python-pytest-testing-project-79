import pytest
import tempfile
import os
import requests_mock
from page_loader import download


@pytest.mark.asyncio
async def test_bad_http_status():
    with tempfile.TemporaryDirectory() as tmpdirname:
        with requests_mock.Mocker() as m:
            m.get(
                "https://ru.hexlet.io/courses",
                status_code=404,
            )
            with pytest.raises(Exception):
                download("https://ru.hexlet.io/courses", tmpdirname)
