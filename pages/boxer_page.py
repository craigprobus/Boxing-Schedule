from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.boxer_page_locators import BoxerPageLocators


class BoxerPage:
    def __init__(self, browser):
        self.browser = browser
