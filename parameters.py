# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Edit or modify this file according to needs"

This file contains exposed parameters for the scrapper
contents that are modifiable:
URLS

"""
from datetime import datetime

__all__ = [
	"URLS",
	"get_output_filename",
	"USER_AGENTS",
	"CSV_FILE_FOR_IMAGE_DOWNLOAD",
	"TAKE_CATEGORIES"
]


USER_AGENTS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3"


RANDOMIZE_DOWNLOAD_TIME = True
RANDOMIZE_HEADER = True
TAKE_CATEGORIES = False

# EDITABLE FROM HERE ==========================================================================
URLS = [
	"https://proinvest.trustpass.alibaba.com/productlist.html"
]
OUTPUT_FILENAME = "fixed"
CSV_FILE_FOR_IMAGE_DOWNLOAD = ''


# SOME USEFUL FUNCTIONS =======================================================================
def get_curr_date_time(strft="%b_%d_%Y_%H_%M_%S"):
	return datetime.now().strftime(strft)


def get_output_filename(_name=OUTPUT_FILENAME, extension="csv"):
	return f"{_name}_{get_curr_date_time()}.{extension}"
