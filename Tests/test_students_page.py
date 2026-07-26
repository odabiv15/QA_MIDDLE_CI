from Pages.students_page import StudentsPage
from utils.all_data import AllDate
import allure


class TestStudentsPage:

    @allure.title("Полное заполнение формы регистрации студента")
    def test_fill_form(self, driver):
        page = StudentsPage(driver)
        date = AllDate

        with allure.step("Откыртие страницы регистрации"):
            page.open()

        with allure.step("Заполнение формы"):
            page.close_modal_windows()
            page.input_last_name(date.last_name)
            page.input_first_name(date.first_name)
            page.select_gender(date.gender)
            page.input_mobile(date.mobile)
            page.input_email(date.email)
            page.click_date_of_birth_field()
            page.select_month(date.month)
            page.select_year(date.year)
            page.select_day(date.day)
            page.select_subject(date.subject)
            page.select_hobby(date.hobbies)
            page.input_address(date.address)
            page.select_state_and_city(date.state, date.city)

        with allure.step("Подтверждение заполнения формы"):
            page.click_submit()

        with allure.step("Проверка отображения текста об успешном заполении формы"):
            text = page.get_result_table()
            assert text == date.result_table_text, "Некорректно заполнена форма, текст не отображается"




