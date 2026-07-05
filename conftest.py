import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Tests.test_github import is_desktop_aspect

SELENOID_URL = "https://user1:1234@selenoid.autotests.cloud/wd/hub"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Remote(
        command_executor=SELENOID_URL,
        options=options,
    )
    yield driver
    driver.quit()


@pytest.fixture
def viewport(request, driver):
    width, height, platform = request.param
    driver.set_window_size(width, height)

    if platform == "mobile" and is_desktop_aspect(width, height):
        pytest.skip("Mobile-тест при desktop aspect ratio")
    if platform == "desktop" and not is_desktop_aspect(width, height):
        pytest.skip("Desktop-тест при mobile aspect ratio")

    return {
        "width": width,
        "height": height,
        "platform": platform,
    }


@pytest.fixture
def desktop_setup(driver):
    driver.set_window_size(1920, 1080)
    return driver


@pytest.fixture
def mobile_setup(driver):
    driver.set_window_size(375, 812)
    return driver
