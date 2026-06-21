from Pages.login_page import LoginPage

class TestLoginPage:
    url = "https://qa-guru.github.io/one-page-form/login"

    def open(self, driver):
        driver.get(self.url)

    def test_empty_fill_and_login(self, driver):
        page = LoginPage(driver)

        self.open(driver)
        page.click_login_button()
        message_text = page.get_error_message()
        assert message_text == "Login and password are required (minimum 3 and 6 characters)"

    def test_incorrect_number_of_characters_in_login(self, driver):
        page = LoginPage(driver)

        self.open(driver)
        page.input_login_field("1")
        page.input_password_field("qwerty")
        page.click_login_button()
        message_text = page.get_error_message()
        assert message_text == "Login must be at least 3 characters"

    def test_incorrect_number_of_characters_in_password(self, driver):
        page = LoginPage(driver)

        self.open(driver)
        page.input_login_field("qwerty")
        page.input_password_field("1")
        page.click_login_button()
        message_text = page.get_error_message()
        assert message_text == "Password must be at least 6 characters"





