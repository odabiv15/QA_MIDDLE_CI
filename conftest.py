import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.client_config import ClientConfig
from utils import attache

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        default="https://qa-guru.github.io/one-page-form/automation-practice-form.html",
        help="URL тестируемого сайта",
    )
    parser.addoption(
        "--selenoid_url",
        default="https://selenoid.qa.guru/wd/hub",
        help="URL удалённого браузера (Selenoid)",
    )
    parser.addoption(
        "--browser",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Браузер",
    )
    parser.addoption("--browser_version", default="128.0", help="Версия браузера в Selenoid")
    parser.addoption(
        "--headless",
        default="false",
        choices=("true", "false"),
        help="Headless режим",
    )
    parser.addoption(
        "--window_size",
        default="1920,1080",
        help="Разрешение экрана, формат WIDTH,HEIGHT",
    )
    parser.addoption(
        "--remote",
        default="false",
        choices=("true", "false"),
        help="Запуск через Selenoid (true) или локально (false)",
    )


@pytest.fixture(scope="session")
def base_url(request):
    url = request.config.getoption("--base_url")
    print(f"\n[config] base_url = {url}")
    return url


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    headless = request.config.getoption("--headless") == "true"
    window_size = request.config.getoption("--window_size")
    selenoid_url = request.config.getoption("--selenoid_url")
    remote = request.config.getoption("--remote") == "true"

    # Секреты — только из .env
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_password = os.getenv("SELENOID_PASSWORD")

    if browser_name == "firefox":
        options = FirefoxOptions()
    else:
        options = ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    options.add_argument(f"--window-size={window_size}")
    if headless:
        options.add_argument("--headless")

    if remote:
        options.browser_version = browser_version
        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": True,
            },
        )
        client_config = ClientConfig(
            remote_server_addr=selenoid_url,
            username=selenoid_login,
            password=selenoid_password,
        )
        browser = webdriver.Remote(
            command_executor=selenoid_url,
            options=options,
            client_config=client_config,
        )
    else:
        if browser_name == "firefox":
            browser = webdriver.Firefox(options=options)
        else:
            browser = webdriver.Chrome(options=options)

    yield browser

    attache.add_screenshot(browser)
    attache.add_page_source(browser)
    if browser_name == "chrome":
        attache.add_console_logs(browser)
    if remote:
        attache.add_video(browser, selenoid_url)
    browser.quit()
