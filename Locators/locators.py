from selenium.webdriver.common.by import By


class PageLocators:
    # https://qa-guru.github.io/one-page-form/automation-practice-form.html

    PRACTICE_FORM = (By.XPATH, "//form[@id='userForm']")

    # text fields
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    MOBILE = (By.XPATH, "//input[@id='userNumber']")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput']")
    SUBJECTS_INPUT = (By.XPATH, "//input[@id='subjectsInput']")
    SUBJECTS_VALUE = (By.XPATH, "//input[@id='subjectsValue']")
    SUBJECTS_CHIPS = (By.XPATH, "//div[@id='subjectsChips']")
    UPLOAD_PICTURE = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    STATE_VALUE = (By.XPATH, "//input[@id='stateValue']")
    CITY_VALUE = (By.XPATH, "//input[@id='cityValue']")

    # gender (radio)
    GENDER_MALE = (By.XPATH, "//input[@id='gender-radio-1']")
    GENDER_FEMALE = (By.XPATH, "//input[@id='gender-radio-2']")
    GENDER_OTHER = (By.XPATH, "//input[@id='gender-radio-3']")
    GENDER_BY_VALUE = (By.XPATH, "//input[@name='gender' and @value='{}']")

    # hobbies (checkbox)
    HOBBY_SPORTS = (By.XPATH, "//input[@id='hobbies-checkbox-1']")
    HOBBY_READING = (By.XPATH, "//input[@id='hobbies-checkbox-2']")
    HOBBY_MUSIC = (By.XPATH, "//input[@id='hobbies-checkbox-3']")
    HOBBY_BY_VALUE = (By.XPATH, "//input[@type='checkbox' and @value='{}']")

    # state / city (custom dropdown)
    STATE = (By.XPATH, "//div[@id='state']")
    CITY = (By.XPATH, "//div[@id='city']")
    STATE_CITY_DROPDOWN = (By.XPATH, "//div[@id='stateCity-wrapper']//div[text()='{}']")
    STATE_CITY_OPTION = (By.XPATH, "//div[@id='stateCity-wrapper']//div[text()='{}']")

    # subjects autocomplete
    SUBJECTS_DROPDOWN = (By.XPATH, "//div[@id='subjectsDropdown']")
    SUBJECTS_OPTION = (By.XPATH, "//div[@id='subjectsDropdown']//div[text()='{}']")

    # datepicker
    DATEPICKER_MONTH = (By.XPATH, "//select[contains(@class,'react-datepicker__month-select')]")
    DATEPICKER_YEAR = (By.XPATH, "//select[contains(@class,'react-datepicker__year-select')]")
    DATEPICKER_DAY = (
        By.XPATH,
        "//div[@id='datepickerDays']//div[contains(@class,'react-datepicker__day') "
        "and not(contains(@class,'outside-month')) and text()='{}']",
    )

    # buttons
    SUBMIT = (By.XPATH, "//button[@id='submit']")
    CLOSE_MODAL = (By.XPATH, "//button[@aria-label='Close']")

    # result modal
    RESULT_MODAL = (By.XPATH, "//dialog[@id='resultModal']")
    RESULT_MODAL_TITLE = (By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
    RESULT_BODY = (By.XPATH, "//div[@id='example-modal-sizes-title-lg']")
    FORM_ERROR = (By.XPATH, "//p[@id='formError']")
