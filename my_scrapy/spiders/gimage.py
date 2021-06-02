import scrapy
from bs4 import BeautifulSoup


class GimageSpider(scrapy.Spider):
    name = 'gimage'
    allowed_domains = ['www.google.com.tw/imghp']
    start_urls = ['https://www.google.com.tw/imghp?hl=zh-TW&ogbl']

    def parse(self, response):
      soup = BeautifulSoup(response.text, 'lxml')
      
      # print(ele)