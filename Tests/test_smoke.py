from utils.all_data import AllData


def test_all_data_email_is_set():
    assert AllData.email_user == "g.maleryan@mail.ru"


def test_all_data_name_is_set():
    assert "Генрик" in AllData.fill_name


def test_pytest_collects_project_modules():
    from Pages.box_page import PageBox
    from Base.Base_class import Base

    assert PageBox is not None
    assert Base is not None
