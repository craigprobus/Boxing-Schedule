from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.boxer_page_locators import BoxerPageLocators


class BoxerCardParser:
    def __init__(self, parent_element):
        self.parent_element = parent_element

    @property
    def url(self):
        return self.parent_element.get_attribute('data-url')

    @property
    def boxer_name(self):
        WebDriverWait(self.parent_element, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, BoxerPageLocators.BOXER_NAME)
            )
        )
        return self.parent_element.find_element(By.CSS_SELECTOR, BoxerPageLocators.BOXER_NAME).text

    @property
    def boxer_ranking(self):
        WebDriverWait(self.parent_element, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, BoxerPageLocators.RANKING)
            )
        )
        return self.parent_element.find_element(By.CSS_SELECTOR, BoxerPageLocators.RANKING).text