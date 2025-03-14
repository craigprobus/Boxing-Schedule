from selenium.webdriver.common.by import By

from locators.boxer_page_locators import BoxerPageLocators


class WeightDivisionPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def weight_classes(self):
        elements = self.browser.find_elements(By.CSS_SELECTOR, BoxerPageLocators.WEIGHT_CLASS_MENU_ITEM)
        return elements
