import allure

from utils.all_data import AllData


@allure.title("Проверка email в тестовых данных")
@allure.severity(allure.severity_level.MINOR)
def test_all_data_email_is_set():
    with allure.step("Проверка значения email"):
        assert AllData.email_user == "g.maleryan@mail.ru"


@allure.title("Проверка имени в тестовых данных")
@allure.severity(allure.severity_level.MINOR)
def test_all_data_name_is_set():
    with allure.step("Проверка наличия имени в Full Name"):
        assert "Генрик" in AllData.fill_name


@allure.title("Проверка импорта модулей проекта")
@allure.severity(allure.severity_level.MINOR)
def test_pytest_collects_project_modules():
    with allure.step("Импорт Page Object и Base"):
        from Pages.box_page import PageBox
        from Base.Base_class import Base

        assert PageBox is not None
        assert Base is not None
