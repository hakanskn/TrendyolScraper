import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.remote.webelement import WebElement
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import pandas as pd
import random
from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager
from product import *


class ProductProvider(object):

    @staticmethod
    def GetPageProducts(visit_url):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_argument('--headless')

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        # browser = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
        browser.get(visit_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 30)

        # time.sleep(5)

        ActionChains(browser).move_by_offset(0, 0).click().perform()
        time.sleep(1)

        # i = 1
        # soup = BeautifulSoup(browser.page_source, 'html.parser')
        # while True:
        #     print(str(i) + " scrolling...")
        #     browser.execute_script("window.scrollTo(0, window.scrollY + 500)")
        #     soup1 = BeautifulSoup(browser.page_source, 'html.parser')
        #
        #     if (soup1.prettify() == soup.prettify() and i % 5 == 0):
        #         break
        #
        #     soup = soup1
        #     i += 1

        for i in range(1, 20001):
            browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
            time.sleep(0.3)

            if (i % 10 == 0):
                print(str(i) + " scrolling...")
                soup = BeautifulSoup(browser.page_source, 'html.parser')
                product_container = soup.find('div', attrs={"class": "prdct-cntnr-wrppr"})
                product_item_href_list = product_container.find_all('a')
                item_href_list = [x.get("href") for x in product_item_href_list]
                print("fetched product count: ", len(item_href_list))

        # soup = BeautifulSoup(browser.page_source, 'html.parser')
        # product_container = soup.find('div', attrs={"class": "prdct-cntnr-wrppr"})
        # product_item_href_list = product_container.find_all('a')
        # item_href_list = [x.get("href") for x in product_item_href_list]


        return item_href_list