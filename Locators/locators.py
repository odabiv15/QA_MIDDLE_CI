from selenium.webdriver.common.by import By


class PageLocators:

#LOCARORS TEXT BOX FORM

    full_name = (By.XPATH, "//*[@id='userName']")
    email = (By.XPATH, "//*[@id='userEmail']")
    current_address = (By.XPATH, "//*[@id='currentAddress']")
    permanent_address = (By.XPATH, "//*[@id='permanentAddress']")
    submit_button = (By.XPATH, "//*[@id='submit']")
    result_text_field = (By.XPATH, "//div[@id='output']")
    email_text = (By.XPATH, "//*[@id='email']")

#LOCATORS_LOGIN_FORM

    LOGIN_FIELD = (By.XPATH, "//input[@id='login-input']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password-input']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='Login']")
    STATUS_MESSAGE = (By.XPATH, "//p[@id='error-message']")



#LOCATORS STUDENTS REGISTRATIONS FORM