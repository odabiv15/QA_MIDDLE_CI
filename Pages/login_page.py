from QA_MIDDLE_CI.Base.Base_class import Base
from QA_MIDDLE_CI.Locators.locators import PageLocators


class LoginPage(Base):

    def click_login_button(self):
        self.click(PageLocators.LOGIN_BUTTON)

    def input_login_field(self, text):
        self.input(PageLocators.LOGIN_FIELD, text)

    def input_password_field(self, text):
        self.input(PageLocators.PASSWORD_FIELD, text)

    def get_error_message(self):
        return self.get_text(PageLocators.STATUS_MESSAGE)
