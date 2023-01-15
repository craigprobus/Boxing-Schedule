from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.boxer_page_locators import BoxerPageLocators
from parsers.boxer_card_parser import BoxerCardParser

class BoxerPage:
    def __init__(self, browser):
        self.browser = browser

    def boxer_cards(self) -> List[BoxerCardParser]:
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, BoxerPageLocators.BOXER_CARD)
            )
        )
        cards = self.browser.find_elements(By.CSS_SELECTOR, BoxerPageLocators.BOXER_CARD)
        return [BoxerCardParser(card) for card in cards]
