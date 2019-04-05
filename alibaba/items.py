# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlibabaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    min_order = scrapy.Field()
    payment = scrapy.Field()
    quick_details = scrapy.Field()
    supply_ability = scrapy.Field()
    packaging_delivery = scrapy.Field()
    product_description = scrapy.Field()
    url = scrapy.Field()
    images_links = scrapy.Field()
    # category
    # images links
    # price
    # min Order
    # Payment
    # quick details
    # supply ability
    # packaging and delivery
    # Product Description
