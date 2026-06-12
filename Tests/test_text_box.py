import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
#locators

    full_name = (By.XPATH, "//*[@id='userName']")
    email = (By.XPATH, "//*[@id='userEmail']")
    current_address = (By.XPATH, "//*[@id='currentAddress']")
    permanent_address = (By.XPATH, "//*[@id='permanentAddress']")
    submit_button = (By.XPATH, "//*[@id='submit']")
    result_text_field = (By.XPATH, "//div[@id='output']")
    email_text = (By.XPATH, "//*[@id='email']")

#utils
    fill_name = "Малерян Генрик Василевич"
    email_user = "g.maleryan@mail.ru"
    invalid_email = "123"
    current_address_user = "Привокальная 3/1"
    permanent_address_user = "Хутро Балабино-Русский"


#methods
    def set_up(self):
        self.driver = webdriver.Chrome()
        url = "https://qa-guru.github.io/one-page-form/text-box.html"
        self.driver.get(url)
        self.driver.maximize_window()

    def input_fill_name(self, name):
        element = self.driver.find_element(*self.full_name)
        element.send_keys(name)

    def input_email(self, email):
        element = self.driver.find_element(*self.email)
        element.send_keys(email)

    def input_permanent_address(self, address):
        element = self.driver.find_element(*self.permanent_address)
        element.send_keys(address)

    def input_current_address(self, address):
        element = self.driver.find_element(*self.current_address)
        element.send_keys(address)

    def click_submit(self):
        element = self.driver.find_element(*self.submit_button)
        element.click()

    def get_all_text(self):
        all_text = self.driver.find_element(*self.result_text_field)
        return all_text.text

    def get_email_from_form(self):
        email_text = self.driver.find_element(*self.email_text)
        return email_text.text

    def turn_down(self):
        self.driver.quit()

#tests

    def test_input_fill_name_and_email(self):
        try:
            self.set_up()
            self.input_fill_name(self.fill_name)
            self.input_email(self.email_user)
            self.click_submit()
            all_text = self.get_all_text()
            assert self.email_user in all_text and self.fill_name in all_text, "ФИО и Email некорректно отображаются"

        finally:
            self.turn_down()

    def test_input_all_field(self):
        try:

            self.set_up()
            self.input_fill_name(self.fill_name)
            self.input_email(self.email_user)
            self.input_current_address(self.current_address_user)
            self.input_permanent_address(self.permanent_address_user)
            self.click_submit()
            all_text = self.get_all_text()
            assert self.email_user in all_text, "Email некорректно отображается"
            assert self.fill_name in all_text, "ФИО некорректно отображается"
            assert self.current_address_user in all_text, "Текущий адресс некорректно отображается"
            assert self.permanent_address_user in all_text, "Постоянный адресс некорректно отображается"

        finally:
            self.turn_down()

    def test_checking_email_control(self):
        try:
            self.set_up()
            self.input_email(self.invalid_email)
            self.click_submit()

            elements = self.driver.find_elements(*self.email_text)

            if len(elements) > 0:
                assert not elements[0].is_displayed(), "Контроль не сработал, текст почты виден"

        finally:
            self.turn_down()

