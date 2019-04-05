# -*- coding: utf-8 -*-
# from parameters import *
from scrapy import Spider


class AlibabaSpiderSpider(Spider):

    def __init__(self, **kwargs):
        super(AlibabaSpiderSpider, self).__init__(**kwargs)
        self.allowed_domains = ['alibaba.com']
        self.name = 'alibaba-spider'
        self.start_urls = kwargs.get("urls")

    def parse(self, response):
        # first parse for url link
        links = response.xpath('//div[@class="product-info"]/div[@class="title"]/a/@href').extract()
        # process and remove extra links
        for i in range(0, 8):
            links.pop(0)

        for j in links:
            print(j)
        # next
        next_page_url = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page_url:
            yield response.follow(next_page_url)


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
