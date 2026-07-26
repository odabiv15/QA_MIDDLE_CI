import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SELENOID_URL = "https://user1:1234@selenoid.autotests.cloud/wd/hub"


def _use_selenoid():
    return os.getenv("USE_SELENOID", "").lower() in ("1", "true", "yes")


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    if _use_selenoid():
        browser = webdriver.Remote(
            command_executor=SELENOID_URL,
            options=options,
        )
    else:
        browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
