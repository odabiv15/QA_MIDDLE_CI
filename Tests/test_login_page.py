import pytest

from Pages.login_page import LoginPage


class TestLoginPage:
    url = "https://qa-guru.github.io/one-page-form/login"

    def open(self, driver):
        driver.get(self.url)

    @pytest.mark.parametrize(
        "login, password, expected_message",
        [
            (
                "",
                "",
                "Login and password are required (minimum 3 and 6 characters)",
            ),
            (
                "1",
                "qwerty",
                "Login must be at least 3 characters",
            ),
            (
                "qwerty",
                "1",
                "Password must be at least 6 characters",
            ),
        ],
        ids=["empty_fields", "short_login", "short_password"],
    )
    def test_login_validation_errors(self, driver, login, password, expected_message):
        page = LoginPage(driver)
        self.open(driver)

        if login:
            page.input_login_field(login)
        if password:
            page.input_password_field(password)

        page.click_login_button()
        message_text = page.get_error_message()

        assert message_text == expected_message