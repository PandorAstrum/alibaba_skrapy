# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Run this file from command line"

This file contains the mechanism to run the scrapper when called
It is called from command line (CMD in Windows or BASH on LINUX)
"""
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from alibaba.spiders import alibaba_spiders
from parameters import *

sys.path.append('.\\alibaba\\alibaba\\spiders\\')


def main():
	_project_settings = get_project_settings()
	process = CrawlerProcess(_project_settings)

	output = get_output_filename()
	process.settings.update({
		'FEED_URI': output,
		'LOG_LEVEL': 'INFO',
	})
	# _project_settings.update()
	process.crawl(alibaba_spiders.AlibabaSpidersSpider, _start_urls=URLS, _headers=USER_AGENTS, _take_categories=TAKE_CATEGORIES)

	process.start()  # the script will block here until the crawling is finished


if __name__ == '__main__':
	main()
