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
        self.start_urls = [kwargs.get('_start_urls')]
        self.headers = kwargs.get('_headers')
        self.category_check = kwargs.get('_category_check')
        self.prev = kwargs.get('_prev')
        self.previous_list = kwargs.get('_previous_list')
        self.tmp_links = []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers={'User-Agent': self.headers})

    def parse(self, response):
        if self.category_check:
            # only scrap the categories
            categories = response.xpath('//div[@class="mod-content"]//ul//li//a/text()').extract()
            # write to file
            all_sub_cat = response.xpath('//div[@module-title="productGroups"]/@module-data').extract_first()
            all_sub_cat = all_sub_cat.replace('%', ',').replace('0', ',').replace('1', ',').replace('2', ',')
            all_sub_cat = all_sub_cat.replace('3', ',').replace('4', ',').replace('5', ',').replace('6', ',')
            all_sub_cat = all_sub_cat.replace('7', ',').replace('8', ',').replace('9', ',')
            all_sub_cat_spit = all_sub_cat.split('Fproductgrouplist')
            all_sub_cat_spit.pop(0)
            # print(all_sub_cat_spit)
            for c in categories:
                subs = []
                cat_ = []
                if '&' in c:
                    matching_category = c.replace('&', '_').replace(' ', '')
                elif " " in c:
                    matching_category = c.replace(' ', '_')
                elif ',' in c:
                    matching_category = c.replace(',', '').replace(' ', '_')
                elif '/' in c:
                    matching_category = c.replace('&', '').replace(',', '').replace(' ', '_')
                else:
                    matching_category = c

                for indx, sub in enumerate(all_sub_cat_spit):
                    sub_cat = re.findall(r'([A-Z]\w+\.html)', sub)
                    sub_cat[0] = sub_cat[0].replace('.html', '').replace('F', '', 1)

                    if sub_cat[0] == matching_category:
                        cat_.append(sub_cat[0])
                        break
                    else:
                        subs.append(sub_cat[0])

                for s in all_sub_cat_spit[:]:
                    sub_cat = re.findall(r'([A-Z]\w+\.html)', s)
                    sub_cat[0] = sub_cat[0].replace('.html', '').replace('F', '', 1)
                    if sub_cat[0] in subs:
                        all_sub_cat_spit.remove(s)
                    if sub_cat[0] in cat_:
                        all_sub_cat_spit.remove(s)

                yield {
                    "Category": matching_category,
                    "Sub Category": subs
                }

        else:
            # get all the links
            _div = response.xpath('//div[@class="module-product-list"]')

            links = _div.xpath('.//div[@class="product-info"]/div[@class="title"]/a/@href').extract()
            # process and remove extra links
            for link in links:
                if link not in self.tmp_links:
                    abs_link = response.urljoin(link)
                    self.tmp_links.append(abs_link)
                    yield Request(url=abs_link, callback=self.parse_item, headers={'User-Agent': self.headers})
            # next
            next_page_url = response.xpath('//div[@class="next-pagination-list"]/a/@href').extract()
            for next_page in next_page_url:
                if next_page:
                    abs_next_page_url = response.urljoin(next_page)
                    yield Request(abs_next_page_url, callback=self.parse, headers={'User-Agent': self.headers})

    def parse_item(self, response):
        # get actual data here
        soup = BeautifulSoup(response.text, 'lxml')
        item = AlibabaItem()
        # if previous file then get the list of previous url and match
        if not self.prev:
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
            item['supply_ability'] = response.xpath(
                '//div[contains(text(), "Supply Ability")]/following-sibling::div/dl/dd/text()').extract_first()
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
                # clean

                for i, t in enumerate(_tmp_packaging):
                    if "Lead Time" in t:
                        removing_index = i
                    else:
                        removing_index = None

                if removing_index is None:
                    pass
                else:
                    _tmp_packaging = _tmp_packaging[:removing_index]

                item['packaging_delivery'] = _tmp_packaging

            _desc = soup.find('div', {'id': 'J-rich-text-description'})
            _desc_div = _desc.find('div', {'data-section-title': "Product Description"})
            if _desc_div:
                _all_description = _desc_div.findAll('p')
                if len(_all_description) == 0:
                    _d = _desc.prettify().replace('\n', '')
                    _d = ''.join(c for c in _d if ord(c) < 128)
                    tmp_description = _d  # no p
                else:
                    tmp_description = []
                    # get temp descriptions
                    for _description in _all_description:
                        _d = _description.prettify().replace('\n', '')
                        if "<img" not in _d:
                            _d = ''.join(c for c in _d if ord(c) < 128)
                            # dump any image
                            tmp_description.append(_d)

                    index_of_related_products = 0
                    # find related products
                    for indx, td in enumerate(tmp_description):
                        if re.search(r'[r|R]elated [p|P]roducts', td) is not None:
                            index_of_related_products = indx
                            break
                        else:
                            index_of_related_products = len(tmp_description) + 1
                    # slicing only take upto related products clean
                _final_desc = tmp_description[:index_of_related_products]
                # joining list elements into one string
                _joined_string_description = ''.join(_final_desc)

            else:
                _all_description = _desc.findAll('p')
                if len(_all_description) == 0:
                    _d = _desc.prettify().replace('\n', '')
                    _d = ''.join(c for c in _d if ord(c) < 128)
                    tmp_description = _d
                else:
                    tmp_description = []

                    # get into a list
                    for _description in _all_description:
                        _d = _description.prettify().replace('\n', '')
                        if "<img" not in _d:
                            _d = ''.join(c for c in _d if ord(c) < 128)
                        # dump any image
                            tmp_description.append(_d)

                    index_of_related_products = 0
                    # find related products
                    for indx, td in enumerate(tmp_description):
                        if re.search(r'[r|R]elated [p|P]roducts', td) is not None:
                            index_of_related_products = indx
                            break
                        else:
                            index_of_related_products = len(tmp_description) + 1
                        # clean
                _final_desc = tmp_description[:index_of_related_products]
                # joining list elements into one string
                _joined_string_description = ''.join(_final_desc)
            item['description'] = _joined_string_description
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
        else:
            if response.url not in self.previous_list:
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
                item['supply_ability'] = response.xpath(
                    '//div[contains(text(), "Supply Ability")]/following-sibling::div/dl/dd/text()').extract_first()
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
                    # clean

                    for i, t in enumerate(_tmp_packaging):
                        if "Lead Time" in t:
                            removing_index = i
                        else:
                            removing_index = None

                    if removing_index is None:
                        pass
                    else:
                        _tmp_packaging = _tmp_packaging[:removing_index]

                    item['packaging_delivery'] = _tmp_packaging

                _desc = soup.find('div', {'id': 'J-rich-text-description'})
                _desc_div = _desc.find('div', {'data-section-title': "Product Description"})
                if _desc_div:
                    _all_description = _desc_div.findAll('p')
                    if len(_all_description) == 0:
                        _d = _desc.prettify().replace('\n', '')
                        _d = ''.join(c for c in _d if ord(c) < 128)
                        tmp_description = _d  # no p
                    else:
                        tmp_description = []
                        # get temp descriptions
                        for _description in _all_description:
                            _d = _description.prettify().replace('\n', '')
                            if "<img" not in _d:
                                _d = ''.join(c for c in _d if ord(c) < 128)
                                # dump any image
                                tmp_description.append(_d)

                        index_of_related_products = 0
                        # find related products
                        for indx, td in enumerate(tmp_description):
                            if re.search(r'[r|R]elated [p|P]roducts', td) is not None:
                                index_of_related_products = indx
                                break
                            else:
                                index_of_related_products = len(tmp_description) + 1
                        # slicing only take upto related products clean
                    _final_desc = tmp_description[:index_of_related_products]
                    # joining list elements into one string
                    _joined_string_description = ''.join(_final_desc)
                else:
                    _all_description = _desc.findAll('p')
                    if len(_all_description) == 0:
                        _d = _desc.prettify().replace('\n', '')
                        _d = ''.join(c for c in _d if ord(c) < 128)
                        tmp_description = _d
                    else:
                        tmp_description = []

                        # get into a list
                        for _description in _all_description:
                            _d = _description.prettify().replace('\n', '')
                            if "<img" not in _d:
                                _d = ''.join(c for c in _d if ord(c) < 128)
                                # dump any image
                                tmp_description.append(_d)

                        index_of_related_products = 0
                        # find related products
                        for indx, td in enumerate(tmp_description):
                            if re.search(r'[r|R]elated [p|P]roducts', td) is not None:
                                index_of_related_products = indx
                                break
                            else:
                                index_of_related_products = len(tmp_description) + 1
                            # clean
                    _final_desc = tmp_description[:index_of_related_products]
                    # joining list elements into one string
                    _joined_string_description = ''.join(_final_desc)
                item['description'] = _joined_string_description
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
