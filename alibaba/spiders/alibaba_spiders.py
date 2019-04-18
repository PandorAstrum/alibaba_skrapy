# -*- coding: utf-8 -*-
import re
from scrapy import Request
from scrapy import Spider
from bs4 import BeautifulSoup
from alibaba.items import AlibabaItem


class AlibabaSpidersSpider(Spider):
    name = 'alibaba_spiders'
    allowed_domains = ['alibaba.com']

    def __init__(self, **kwargs):
        super(AlibabaSpidersSpider, self).__init__(**kwargs)
        self.start_urls = kwargs.get('_start_urls')
        self.headers = kwargs.get('_headers')
        self.take_categories = kwargs.get('_take_categories')
        self.tmp_links = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers={'User-Agent': self.headers})

    def parse(self, response):
        if self.take_categories:
            # only scrap the categories
            catagories = response.xpath('//div[@class="mod-content"]//ul//li//a/text()').extract()
            # write to file
            pass
        else:
            # get all the links
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
        soup = BeautifulSoup(response.text, 'lxml')
        item = AlibabaItem()

        item['url'] = response.url

        item['title'] = response.xpath('//h1[@class="ma-title"]/text()').extract_first()

        item['price'] = response.xpath('//span[@class="ma-ref-price"]/span/text()').extract_first()

        item['min_order'] = response.xpath('//span[@class="ma-min-order"]/text()').extract_first()

        _quick_details = response.xpath('//div[contains(text(), "Quick Details")]/following-sibling::div/dl')
        _q1_keys = _quick_details.xpath('.//dt/span/text()').extract()
        _q2_values = _quick_details.xpath('.//dd/div/text()').extract()
        _q = list(zip(_q1_keys, _q2_values))  # need to arrange in str format
        tmp_quick_details = []
        for quick in _q:
            tmp_quick_details.append("\n" + quick[0] + " " + quick[1])

        tmp_quick_details[0] = tmp_quick_details[0].replace("\n", "")
        item['short_description'] = tmp_quick_details

        item['supply_ability'] = response.xpath('//div[contains(text(), "Supply Ability")]/following-sibling::div/dl/dd/text()').extract_first()

        _packaging = soup.find('div', string='Packaging & Delivery')
        if _packaging:
            _all_packaging_div = _packaging.findNext('div')
            _all_packaging = _all_packaging_div.findAll('dl')
            _tmp_packaging = []
            for _pack in _all_packaging:
                h = _pack.find('dt').text
                t = _pack.find('dd').text
                h.strip()
                t.strip()
                _tmp_packaging.append(h + ": " + t)

            item['packaging_delivery'] = _tmp_packaging

        _desc = soup.find('div', {'id': 'J-rich-text-description'})
        _desc_div = _desc.find('div', {'data-section-title': "Product Description"})
        if _desc_div:
            _all_description = _desc_div.findAll('p')
            if len(_all_description) == 0:
                tmp_description = _desc.prettify() # no p
            else:
                tmp_description = []

            # get into a list
                for _description in _all_description:
                    tmp_description.append(_description.prettify())

                index_of_related_products = 0
            # find related products
                for indx, td in enumerate(tmp_description):
                    x = td
                    if re.search(r'[r|R]elated [p|P]roducts:', x) is not None:
                        index_of_related_products = indx
                    else:
                        index_of_related_products = len(tmp_description) + 1
                # clean
                while len(tmp_description) >= index_of_related_products:
                    tmp_description.pop(-1)

        else:
            _all_description = _desc.findAll('p')
            if len(_all_description) == 0:
                tmp_description = _desc.prettify()
            else:
                tmp_description = []

                # get into a list
                for _description in _all_description:
                    tmp_description.append(_description.prettify())

                index_of_related_products = 0
                # find related products
                for indx, td in enumerate(tmp_description):
                    x = td
                    if re.search(r'[r|R]elated [p|P]roducts:', x) is not None:
                        index_of_related_products = indx
                    else:
                        index_of_related_products = len(tmp_description) + 1
                    # clean
                while len(tmp_description) >= index_of_related_products:
                    tmp_description.pop(-1)

                # tmp = _description.get_text(strip=True)
                # if not tmp == "" or not tmp == " " or not tmp == "\n":
                #     head, sep, tail = tmp.partition('Related Products:')
                #     if "Â" in head:
                #         head = head.replace("Â", "").strip()
                #     tmp_description.append(head)


        item['description'] = tmp_description
        _all_pics_div = soup.find('div', {'class': 'module-detailBoothImage'})
        _all_pic = _all_pics_div.findAll('img')
        _all_pic.pop(0)
        _temp_pic_list = []
        for _pic in _all_pic:
            _tmp_pic = _pic['src']
            _tmp_pic = "https:" + _tmp_pic
            head, sep, tail = _tmp_pic.partition('_50x50')
            _temp_pic_list.append(head)

        item['images_links'] = _temp_pic_list
        yield item
