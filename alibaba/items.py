# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlibabaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    min_order = scrapy.Field()
    short_description = scrapy.Field()
    supply_ability = scrapy.Field()
    packaging_delivery = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    images_links = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
