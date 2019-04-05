# -*- coding: utf-8 -*-
import scrapy
from parameters import *

class AlibabaSpiderSpider(scrapy.Spider):
    name = 'alibaba-spider'
    allowed_domains = ['alibaba.com']
    start_urls = URLS

    def parse(self, response):
        # first parse for url link
        pass

    def parse2(self, response):
        # scrap from those url links

        # product title
        # category
        # images links
        # price
        # min Order
        # Payment
        # quick details
        # supply ability
        # packaging and delivery
        # Product Description
        pass

    def parse_image(self, response):
        # download images
        pass
