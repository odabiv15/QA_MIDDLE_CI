import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _skip_browser_tests():
    if os.getenv("SKIP_BROWSER", "").lower() in ("1", "true", "yes"):
        return True
    if os.getenv("CI") or os.getenv("JENKINS_URL"):
        return True
    return False


@pytest.fixture
def driver():
    if _skip_browser_tests():
        pytest.skip("UI-тесты без браузера (SKIP_BROWSER / CI)")

    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
