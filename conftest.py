import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.client_config import ClientConfig

from utils import attache

SELENOID_URL = "https://selenoid.qa.guru/wd/hub"
SELENOID_USER = "user1"
SELENOID_PASSWORD = "1234"


def _use_selenoid():
    return os.getenv("USE_SELENOID", "").lower() in ("1", "true", "yes")


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    if _use_selenoid():
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True,
        })
        client_config = ClientConfig(
            remote_server_addr=SELENOID_URL,
            username=SELENOID_USER,
            password=SELENOID_PASSWORD,
        )
        browser = webdriver.Remote(
            command_executor=SELENOID_URL,
            options=options,
            client_config=client_config,
        )
    else:
        browser = webdriver.Chrome(options=options)

    yield browser

    attache.add_screenshot(browser)
    attache.add_page_source(browser)
    attache.add_console_logs(browser)
    if _use_selenoid():
        attache.add_video(browser)
    browser.quit()
