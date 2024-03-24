import pytest
import logging


@pytest.fixture()
def go_to_url(selenium):
    def callback(url):
        selenium.get(url)

    return callback
