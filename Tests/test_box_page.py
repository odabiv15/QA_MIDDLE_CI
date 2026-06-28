import time

from Pages.box_page import PageBox
from utils.all_data import AllData


class TestBox:
    url = "https://qa-guru.github.io/one-page-form/text-box.html"

    def open(self, driver):
        driver.get(self.url)

    def test_input_fill_name_and_email(self, driver):
        data_test = AllData
        page = PageBox(driver)

        self.open(driver)
        page.input_full_name(data_test.fill_name)
        page.input_email(data_test.email_user)
        page.click_submit_button()
        all_text = page.get_result_text()
        assert data_test.email_user in all_text, "Email некорректно отображается"
        assert data_test.fill_name in all_text, "ФИО некорректно отображается"

    def test_input_all_field(self, driver):
        data_test = AllData
        page = PageBox(driver)

        self.open(driver)
        page.input_full_name(data_test.fill_name)
        page.input_permanent_address(data_test.permanent_address_user)
        page.input_current_address(data_test.current_address_user)
        page.input_email(data_test.email_user)
        page.click_submit_button()
        all_text = page.get_result_text()
        assert data_test.email_user in all_text, "Email некорректно отображается"
        assert data_test.fill_name in all_text, "ФИО некорректно отображается"
        assert data_test.current_address_user in all_text, "Текущий адресс некорректно отображается"
        assert data_test.permanent_address_user in all_text, "Постоянный адресс некорректно отображается"

    def test_checking_email_control(self, driver):
        data_test = AllData
        page = PageBox(driver)
        from Locators.locators import PageLocators

        self.open(driver)
        page.input_email(data_test.invalid_email)
        page.click_submit_button()

        elements = driver.find_elements(*PageLocators.email_text)

        if len(elements) > 0:
            assert not elements[0].is_displayed(), "Контроль не сработал, текст почты виден"


