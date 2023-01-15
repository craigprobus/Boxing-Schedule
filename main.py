from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.weight_division_page import WeightDivisionPage
from pages.boxer_page import BoxerPage
from data_access_layer import DataAccessLayer

'''
    1) get a List[] of each weight classes (including "Pound for Pound")
    2) loop through all the weight classes and get the ranked boxers in each
    3) write to the DB
'''
RATINGS_URL = 'https://www.ringtv.com/ratings/'
POUND_FOR_POUND = 'POUND FOR POUND'
VACANT = 'VACANT'
try:
    chrome_weight_divisions = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # set up selenium
    chrome_boxers = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_weight_divisions.get(RATINGS_URL)
    weight_division_page = WeightDivisionPage(chrome_weight_divisions)
    weight_classes = weight_division_page.weight_classes
    p4p_weight_division = None
    dal = DataAccessLayer()
    for wc in weight_classes:
        url = wc.get_attribute('data-href')
        weight_division_name = wc.text.split('\n')[0]
        if POUND_FOR_POUND == weight_division_name:  # add to P4P to separate List[] and process after other divisions
            p4p_weight_division = wc
            continue
        chrome_boxers.get(url)
        boxer_page = BoxerPage(chrome_boxers)
        boxer_cards = boxer_page.boxer_cards()
        for bc in boxer_cards:
            if VACANT == bc.boxer_name:
                continue
            print(f'{weight_division_name} :: {bc.boxer_ranking}) {bc.boxer_name} :: {bc.boxer_ranking}')
            # dal.insert_boxer(weight_division_name, bc)
    # loop through the P4P boxers... perform an UPDATE operation instead of an INSERT
    p4p_url = p4p_weight_division.get_attribute('data-href')
    print(f'P4P :: NAVIGATING TO {p4p_url}...')
    chrome_boxers.get(p4p_url)
    boxer_page = BoxerPage(chrome_boxers)
    boxer_cards = boxer_page.boxer_cards()
    print(f'P4P :: boxer_cards len <{len(boxer_cards)}>')
    for bc in boxer_cards:
        boxer_record_upd = dal.get_p4p_boxers(bc.boxer_name)
        print(f'boxer_record_upd.id {boxer_record_upd[0][0]}')
        dal.update_boxer_p4p_ranking(boxer_record_upd[0][0], bc.boxer_ranking)
    input('Press any button to complete: ')
except Exception as e:
    print(e)