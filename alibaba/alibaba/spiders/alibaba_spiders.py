# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import Spider
from ..items import AlibabaItem

class AlibabaSpidersSpider(Spider):
    name = 'alibaba_spiders'
    allowed_domains = ['alibaba.com']

    def __init__(self, **kwargs):
        super(AlibabaSpidersSpider, self).__init__(**kwargs)
        self.start_urls = kwargs.get('_start_urls')
        self.headers = kwargs.get('_headers')
        self.tmp_links = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers={'User-Agent': self.headers})

    # name = 'alibaba_spiders'
    # allowed_domains = ['alibaba.com']
    # start_urls = ["https://proinvest.trustpass.alibaba.com/productlist.html"]

    def parse(self, response):

        # first parse to get all the links
        links = response.xpath('//div[@class="product-info"]/div[@class="title"]/a/@href').extract()
        # process and remove extra links
        for link in links:
            if link not in self.tmp_links:
                print(link)
                abs_link = response.urljoin(link)
                self.tmp_links.append(abs_link)

        # next
        next_page_url = response.xpath('//div[@class="next-pagination-list"]/a/@href').extract()
        for next_page in next_page_url:

            if next_page:
                abs_next_page_url = response.urljoin(next_page)
                yield Request(abs_next_page_url, callback=self.parse, headers={'User-Agent': self.headers})

        for tmp_link in self.tmp_links:
            yield Request(tmp_link, callback=self.parse2, headers={'User-Agent': self.headers})

    def parse2(self, response):
        # get actual data here
        item = AlibabaItem()
        item['url'] = response.url
        item['product_name'] = ''
        item['category'] = ''
        item['price'] = ''
        item['min_order'] = ''
        item['payment'] = ''
        item['quick_details'] = ''
        item['supply_ability'] = ''
        item['packaging_delivery'] = ''
        item['product_description'] = ''
        item['images_links'] = ''
        print(response)
        yield item
