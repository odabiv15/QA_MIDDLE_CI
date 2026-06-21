from QA_MIDDLE_CI.Base.Base_class import Base
from QA_MIDDLE_CI.Locators.locators import PageLocators


class PageBox(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def input_full_name(self, text):
        self.input(PageLocators.full_name, text)

    def input_email(self, text):
        self.input(PageLocators.email, text)

    def input_current_address(self, text):
        self.input(PageLocators.current_address, text)

    def input_permanent_address(self, text):
        self.input(PageLocators.permanent_address, text)

    def click_submit_button(self):
        self.click(PageLocators.submit_button)

    def get_result_text(self):
        return self.get_text(PageLocators.result_text_field)

    def get_email_text(self):
        return self.get_text(PageLocators.email_text)
