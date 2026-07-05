import allure

from Pages.box_page import PageBox
from utils.all_data import AllData


class TestBox:
    url = "https://qa-guru.github.io/one-page-form/text-box.html"

    def open(self, driver):
        driver.get(self.url)

    @allure.title("Заполнение имени и email с проверкой результата")
    @allure.severity(allure.severity_level.NORMAL)
    def test_input_fill_name_and_email(self, driver):
        data_test = AllData
        page = PageBox(driver)

        with allure.step("Открытие страницы Text Box"):
            self.open(driver)

        with allure.step("Заполнение полей Full Name и Email"):
            page.input_full_name(data_test.fill_name)
            page.input_email(data_test.email_user)

        with allure.step("Отправка формы"):
            page.click_submit_button()

        with allure.step("Проверка отображения введённых данных"):
            all_text = page.get_result_text()
            assert data_test.email_user in all_text, "Email некорректно отображается"
            assert data_test.fill_name in all_text, "ФИО некорректно отображается"

    @allure.title("Заполнение всех полей формы Text Box")
    @allure.severity(allure.severity_level.NORMAL)
    def test_input_all_field(self, driver):
        data_test = AllData
        page = PageBox(driver)

        with allure.step("Открытие страницы Text Box"):
            self.open(driver)

        with allure.step("Заполнение всех полей формы"):
            page.input_full_name(data_test.fill_name)
            page.input_permanent_address(data_test.permanent_address_user)
            page.input_current_address(data_test.current_address_user)
            page.input_email(data_test.email_user)

        with allure.step("Отправка формы"):
            page.click_submit_button()

        with allure.step("Проверка отображения всех введённых данных"):
            all_text = page.get_result_text()
            assert data_test.email_user in all_text, "Email некорректно отображается"
            assert data_test.fill_name in all_text, "ФИО некорректно отображается"
            assert data_test.current_address_user in all_text, "Текущий адресс некорректно отображается"
            assert data_test.permanent_address_user in all_text, "Постоянный адресс некорректно отображается"

    @allure.title("Проверка валидации некорректного email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checking_email_control(self, driver):
        data_test = AllData
        page = PageBox(driver)
        from Locators.locators import PageLocators

        with allure.step("Открытие страницы Text Box"):
            self.open(driver)

        with allure.step("Ввод некорректного email"):
            page.input_email(data_test.invalid_email)

        with allure.step("Отправка формы"):
            page.click_submit_button()

        with allure.step("Проверка, что блок результата не отображается"):
            elements = driver.find_elements(*PageLocators.email_text)

            if len(elements) > 0:
                assert not elements[0].is_displayed(), "Контроль не сработал, текст почты виден"
