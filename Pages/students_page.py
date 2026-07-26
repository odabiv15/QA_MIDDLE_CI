import allure
from selenium.webdriver.common.by import By

from Base.Base_class import Base
from Locators.locators import PageLocators


class StudentsPage(Base):
    URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    @allure.step("Открытие страницы Student Registration Form")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Ввод First Name: {text}")
    def input_first_name(self, text):
        self.input(PageLocators.FIRST_NAME, text)

    @allure.step("Ввод Last Name: {text}")
    def input_last_name(self, text):
        self.input(PageLocators.LAST_NAME, text)

    @allure.step("Ввод Email: {text}")
    def input_email(self, text):
        self.input(PageLocators.EMAIL, text)

    @allure.step("Ввод Mobile: {text}")
    def input_mobile(self, text):
        self.input(PageLocators.MOBILE, text)

    @allure.step("Ввод Date of Birth")
    def click_date_of_birth_field(self):
        self.click(PageLocators.DATE_OF_BIRTH)

    @allure.step("Закрыть модальное окно")
    def close_modal_windows(self):
        self.click(PageLocators.CLOSE_MODAL)

    @allure.step("Выбор месяца из выпадающего списка : {month}")
    def select_month(self, month):
        self.click(PageLocators.DATEPICKER_MONTH)
        month_locator = (By.XPATH, f"//option[text()='{month}']")
        self.click(month_locator)

    @allure.step("Выбор года из выпадающего списка : {year}")
    def select_year(self, year):
        self.click(PageLocators.DATEPICKER_YEAR)
        year_locator = (By.XPATH, f"//option[text()='{year}']")
        self.click(year_locator)

    @allure.step("Выбор дня из календаря : {day}")
    def select_day(self, day):
        self.click(PageLocators.DATEPICKER_YEAR)
        day_locator = (By.XPATH, f"//span[@data-day='{day}']")
        self.click(day_locator)

    @allure.step("Ввод Subjectd : {}")
    def select_subject(self, subject):
        self.click(PageLocators.SUBJECTS_INPUT)
        value_locator = (PageLocators.SUBJECTS_OPTION[0], PageLocators.SUBJECTS_OPTION[1].format(subject))
        self.click(value_locator)

    @allure.step("Ввод Current Address: {text}")
    def input_address(self, text):
        self.input(PageLocators.CURRENT_ADDRESS, text)

    @allure.step("Выбор Gender: {gender}")
    def select_gender(self, gender):
        locator = (PageLocators.GENDER_BY_VALUE[0], PageLocators.GENDER_BY_VALUE[1].format(gender))
        self.click(locator)

    @allure.step("Выбор Hobby: {hobby}")
    def select_hobby(self, hobby):
        locator = (PageLocators.HOBBY_BY_VALUE[0], PageLocators.HOBBY_BY_VALUE[1].format(hobby))
        self.click(locator)

    @allure.step("Выбор State and City: {state}, {city}")
    def select_state_and_city(self, state, city):
        self.click(PageLocators.STATE)
        locator_state = (
            PageLocators.STATE_CITY_OPTION[0],
            PageLocators.STATE_CITY_OPTION[1].format(state),
        )
        self.click(locator_state)
        self.click(PageLocators.CITY)
        locator_city = (
            PageLocators.STATE_CITY_OPTION[0],
            PageLocators.STATE_CITY_OPTION[1].format(city),
        )
        self.click(locator_city)

    @allure.step("Нажатие кнопки Submit")
    def click_submit(self):
        self.click(PageLocators.SUBMIT)

    @allure.step("Получение таблицы результатов")
    def get_result_table(self):
        return self.get_text(PageLocators.RESULT_BODY)
