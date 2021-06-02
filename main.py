# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#   return  '123'

# if(__name__ == '__main__'):
#   app.run()
# import socket
# print(socket.gethostbyname(socket.gethostname()))
# exit()

from my_package.sel_chrome import SelChrome
from my_package.time import MyTime
from bs4 import BeautifulSoup
from my_package.funcs import p

from image_encoder.image_encoder import *
import base64
import time
import os

url = 'https://www.google.com.tw/imghp?hl=zh-TW&ogbl'
chrome = SelChrome('https://www.google.com.tw/imghp?hl=zh-TW&ogbl', br='dev')

chrome.get_el_sumbmit('iu', name='q')
els = chrome.get_el()[0:3]
for el in els:
    el.click()
    time.sleep(2)
    sub_soup = BeautifulSoup(chrome.chrome.page_source, 'html.parser')
    imgs = sub_soup.find_all('img', class_='n3VNCb')
    for img in imgs:
        if 'https' in img.get('src'):
            print(img.get('src'))
    # time.sleep(1)

chrome.quit()
# print(image)
# img_srcs = soup.find_all('img', class_='rg_i Q4LuWd', limit=5)
# for img_src in img_srcs:
