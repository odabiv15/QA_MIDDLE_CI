from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
import pytest


class Base:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def click(self, locators):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators))
        element.click()

    def input(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return text.text




