import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GitHub:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    URL = "https://github.com/"
    SIGN_BUTTON = (By.XPATH, "//a[@href='/login']")

    def click_sign_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SIGN_BUTTON))
        element.click()

    def open_browser(self):
        self.driver.get(self.URL)


def is_desktop_aspect(width, height):
    return width / height > 1.0


class TestGitHub:

    @allure.title("Переход на Sign In GitHub ({platform}, {width}x{height})")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "width, height, platform",
        [
            (1920, 1080, "desktop"),
            (375, 812, "mobile"),
        ],
        ids=["desktop", "mobile"],
    )
    def test_open_github(self, driver, width, height, platform):
        with allure.step(f"Установка размера окна {width}x{height}"):
            driver.set_window_size(width, height)

        page = GitHub(driver)

        with allure.step("Открытие главной страницы GitHub"):
            page.open_browser()

        with allure.step("Нажатие кнопки Sign In"):
            page.click_sign_button()

        with allure.step("Проверка перехода на страницу логина"):
            assert "login" in driver.current_url

    @allure.title("Sign In с пропуском по aspect ratio ({platform}, {width}x{height})")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "width, height, platform",
        [
            (1920, 1080, "desktop"),
            (375, 812, "mobile"),
            (1920, 1080, "mobile"),
            (375, 812, "desktop"),
        ],
        ids=["desktop", "mobile", "mobile_skip", "desktop_skip"],
    )
    def test_sign_in_with_skip(self, driver, width, height, platform):
        with allure.step("Проверка соответствия platform и aspect ratio"):
            if platform == "mobile" and is_desktop_aspect(width, height):
                pytest.skip("Mobile-тест")
            if platform == "desktop" and not is_desktop_aspect(width, height):
                pytest.skip("Desktop-тест")

        with allure.step(f"Установка размера окна {width}x{height}"):
            driver.set_window_size(width, height)

        page = GitHub(driver)

        with allure.step("Открытие главной страницы GitHub"):
            page.open_browser()

        with allure.step("Нажатие кнопки Sign In"):
            page.click_sign_button()

        with allure.step("Проверка перехода на страницу логина"):
            assert "login" in driver.current_url

    @allure.title("Sign In через indirect-фикстуру viewport")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "viewport",
        [
            (1920, 1080, "desktop"),
            (375, 812, "mobile"),
            (1920, 1080, "mobile"),
            (375, 812, "desktop"),
        ],
        indirect=True,
        ids=["desktop_ok", "mobile_ok", "mobile_skip", "desktop_skip"],
    )
    def test_sign_in_indirect(self, driver, viewport):
        allure.dynamic.title(
            f"Sign In indirect ({viewport['platform']}, {viewport['width']}x{viewport['height']})"
        )
        page = GitHub(driver)

        with allure.step(f"Viewport: {viewport['platform']}, {viewport['width']}x{viewport['height']}"):
            pass

        with allure.step("Открытие главной страницы GitHub"):
            page.open_browser()

        with allure.step("Нажатие кнопки Sign In"):
            page.click_sign_button()

        with allure.step("Проверка перехода на страницу логина"):
            assert "login" in driver.current_url

    @allure.title("Sign In на GitHub — desktop")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sign_in_desktop(self, desktop_setup):
        page = GitHub(desktop_setup)

        with allure.step("Открытие главной страницы GitHub (desktop 1920x1080)"):
            page.open_browser()

        with allure.step("Нажатие кнопки Sign In"):
            page.click_sign_button()

        with allure.step("Проверка перехода на страницу логина"):
            assert "login" in desktop_setup.current_url

    @allure.title("Sign In на GitHub — mobile")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sign_in_mobile(self, mobile_setup):
        page = GitHub(mobile_setup)

        with allure.step("Открытие главной страницы GitHub (mobile 375x812)"):
            page.open_browser()

        with allure.step("Нажатие кнопки Sign In"):
            page.click_sign_button()

        with allure.step("Проверка перехода на страницу логина"):
            assert "login" in mobile_setup.current_url
