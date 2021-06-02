from my_package.funcs import p
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SelChrome():
    def __init__(self, url, br):
        if(br=='main'):
          chrome_options = webdriver.ChromeOptions()
          chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
          chrome_options.add_argument("--headless") #無頭模式
          chrome_options.add_argument("--disable-dev-shm-usage")
          chrome_options.add_argument("--no-sandbox")
          self.chrome = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        elif(br=='dev'):
          options = Options()
          options.add_argument("--disable-notifications")
          self.chrome = webdriver.Chrome(
              './chromedriver 2', chrome_options=options)

        self.chrome.get(url)

    def get_el_sumbmit(self, q, **argu):
        for key, value in argu.items():
            attr_name = key
            value = value

        ele = {
                'name': lambda: self.chrome.find_element_by_name(value),
                'id': lambda: self.chrome.find_element_by_id(value)
              }[attr_name]()

        ele.send_keys(q)
           
        ele.submit()

    def get_el(self):
        els = self.chrome.find_elements_by_css_selector('.rg_i')
        return els

    def quit(self):
        self.chrome.quit()
