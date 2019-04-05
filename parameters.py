# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Edit or modify this file according to needs"

This file contains exposed parameters for the scrapper
contents that are modifiable:
URLS

"""
import sys
from datetime import datetime

__all__ = [
	"URLS",
	"URL_LINK_FIXER",
	"XPATH_PRODUCT_LINK",
	"get_output_filename",
	"USER_AGENTS",

]

# put urls here one each line with commas
URLS = [
	"https://proinvest.trustpass.alibaba.com/productlist.html"
]
OUTPUT_FILENAME = "scrapped"
USER_AGENTS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3"
DEEP_LEVEL = 3
REQUEST_HEADERS = ""

PAGINATION_SELECTOR = ""

RANDOMIZE_DOWNLOAD_TIME = True
RANDOMIZE_HEADER = True

URL_LINK_FIXER = "https://proinvest.trustpass.alibaba.com"
XPATH_PRODUCT_LINK = '//div[@class="product-info"]/div[@class="title"]/a/@href'


def get_curr_date_time(strft="%b_%d_%Y_%H_%M_%S"):
	return datetime.now().strftime(strft)


def get_output_filename(_name=OUTPUT_FILENAME, extension="csv"):
	return f"{_name}_{get_curr_date_time()}.{extension}"

