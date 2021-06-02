from my_package.sel_chrome import SelChrome
from my_package.time import MyTime
from bs4 import BeautifulSoup
from my_package.funcs import p

from image_encoder.image_encoder import *
import base64
import time
import os
import socket

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)


line_bot_api = LineBotApi('vKGm6V6xTu0L8rsjiOmg9QjHBz4A47KitZVUGsb6SFT4Ov82fMGQ69drKSgusCSGXBdvfig3mPMl4mntL8ayqt6PxByXjgQdQi32pFKqfes8OcYmRmcd4C9LhyyhHsZ7NHgXkAVT/o8tCnTvKVY3TgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ba2ed4e9669f1e5653349972507e1998')

app = Flask(__name__)

@app.route('/')
def home():
  pass
  # url = 'https://www.google.com.tw/imghp?hl=zh-TW&ogbl'
  # chrome  = SelChrome('https://www.google.com.tw/imghp?hl=zh-TW&ogbl')
  # chrome.get_el_sumbmit('iu', name='q')

  # els = chrome.get_el(attr_name='rg_i Q4LuWd')[0:1]
  # for el in els:
  #   el.click()
  #   time.sleep(1)
  #   sub_soup = BeautifulSoup(chrome.chrome.page_source, 'html.parser')
  #   img = sub_soup.find('img', class_='n3VNCb')  

  # return img.get('src')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    url = 'https://www.google.com.tw/imghp?hl=zh-TW&ogbl'
    chrome  = SelChrome('https://www.google.com.tw/imghp?hl=zh-TW&ogbl', br='main')
    chrome.get_el_sumbmit(event.message.text, name='q')

    els = chrome.get_el()[0:3]
    for el in els:
        el.click()
        time.sleep(2)
        sub_soup = BeautifulSoup(chrome.chrome.page_source, 'html.parser')
        imgs = sub_soup.find_all('img', class_='n3VNCb')
        for img in imgs:
            if 'https' in img.get('src'):
                 line_bot_api.reply_message(
                  event.reply_token,
                  ImageSendMessage(
                    original_content_url=img.get('src'),
                    preview_image_url=img.get('src')
                 ))

    chrome.quit()

if __name__ == "__main__":
    app.run()

