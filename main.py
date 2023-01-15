from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.weight_division_page import WeightDivisionPage
from pages.boxer_page import BoxerPage

'''
    1) get a List[] of each weight classes (including "Pound for Pound")
    2) loop through all the weight classes and get the ranked boxers in each
    3) write to the DB
'''
RATINGS_URL = 'https://www.ringtv.com/ratings/'
try:
    chrome_weight_divisions = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # set up selenium
    chrome_boxers = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_weight_divisions.get(RATINGS_URL)
    weight_division_page = WeightDivisionPage(chrome_weight_divisions)
    weight_classes = weight_division_page.weight_classes
    for wc in weight_classes:
        url = wc.get_attribute('data-href')
        weight_division_name = wc.text.split('\n')[0]
        chrome_boxers.get(url)
        boxer_page = BoxerPage(chrome_boxers)
        boxer_cards = boxer_page.boxer_cards()
        # IF weight_division_name == 'POUND FOR POUND', assign RANKING to P4P
        # IF weight_division_name != 'POUND FOR POUND', assign RANKING to weight_division
        # User index for Ranking
        print(f'{weight_division_name}')  # IF bc.boxer_name == 'VACANT', then continue, do NOT save to DB...
        ranking = 1
        for bc in boxer_cards:
            print('\t' + str(bc.boxer_ranking.replace('C', '0') + ") " + bc.boxer_name + ': ' + bc.url))
            ranking += 1
    input('Press any button to complete: ')
except Exception as e:
    print(e)