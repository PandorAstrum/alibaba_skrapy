# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy import Spider
from alibaba.alibaba.items import AlibabaItem

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

    # start_urls = ["https://proinvest.trustpass.alibaba.com/productlist.html"]
    # headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3"

    def parse(self, response):

        # first parse to get all the links
        links = response.xpath('//div[@class="product-info"]/div[@class="title"]/a/@href').extract()
        # process and remove extra links
        for link in links:
            if link not in self.tmp_links:
                abs_link = response.urljoin(link)
                self.tmp_links.append(abs_link)
                yield Request(url=abs_link, callback=self.parse2, headers={'User-Agent': self.headers})
        # next
        next_page_url = response.xpath('//div[@class="next-pagination-list"]/a/@href').extract()
        for next_page in next_page_url:

            if next_page:
                abs_next_page_url = response.urljoin(next_page)
                yield Request(abs_next_page_url, callback=self.parse, headers={'User-Agent': self.headers})

    def parse2(self, response):
        # get actual data here
        item = AlibabaItem()
        item['url'] = response.url
        item['product_name'] = response.xpath('//h1[@class="ma-title"]/text()').extract_first()
        item['category'] = ''
        item['price'] = response.xpath('//span[@class="ma-ref-price"]/span/text()').extract_first()
        item['min_order'] = response.xpath('//span[@class="ma-min-order"]/text()').extract_first()
        item['payment'] = ''
        _quick_details = response.xpath('//div[contains(text(), "Quick Details")]/following-sibling::div/dl')
        _q1_keys = _quick_details[0].xpath('//dt/span/text()').extract()
        _q2_values = _quick_details[0].xpath('//dd/div/text()').extract()
        _q = dict(zip(_q1_keys, _q2_values))
        item['quick_details'] = _q
        item['supply_ability'] = ''
        item['packaging_delivery'] = ''
        item['product_description'] = ''
        item['images_links'] = ''
        yield item
