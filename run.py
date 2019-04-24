# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "This file contains the mechanism for spider run or download images"
"""
from datetime import datetime
from multiprocessing import Process
import pandas as pd
import requests
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from alibaba.spiders import alibaba_spiders


def get_curr_date_time(strft="%b_%d_%Y_%H_%M_%S"):
	return datetime.now().strftime(strft)


def get_output_filename(_name="", extension="csv"):
	return f"{_name}_{get_curr_date_time()}.{extension}"


def crawl(_output, _delay, _urls, _header, _category_check):
	_project_settings = get_project_settings()
	crawler = CrawlerProcess(_project_settings)
	crawler.settings.update({
		'FEED_URI': _output,
		'FEED_FORMAT': "csv",
		'LOG_LEVEL': 'INFO',
		"DELAY": _delay
	})
	crawler.crawl(alibaba_spiders.AlibabaSpidersSpider, _start_urls=_urls, _headers=_header,
				_category_check=_category_check)
	crawler.start()  # the script will block here until the crawling is finished


def run_scrapper(**kwargs):
	# get all the parameters
	_urls = kwargs.get("urls")
	_header = kwargs.get("header")
	_output_file_name = kwargs.get("output_file_name")
	_output_dir = kwargs.get("output_dir")
	_delay = kwargs.get("delay")
	_category_check = kwargs.get("category_check")
	_update_fn = kwargs.get("update_fn")
	# preprocess parameters
	output = get_output_filename(_name=_output_dir + "/" + _output_file_name)
	_update_fn(_str="Scrapping Data")
	process = Process(target=crawl, args=(output, _delay, _urls, _header, _category_check))
	process.start()
	process.join()


def download_image(_fn, _csv_file, _output_folder):
	# custom methods
	def get_pandas_column(_filepath, _column_name, csv=True):
		if csv:
			df = pd.read_csv(_filepath)
		else:
			df = pd.read_excel(_filepath)
		return df[_column_name]

	def download(url, _dir):
		filename = url.split('/')[-1]
		filename = _dir + filename
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
	# get parameters
	_image_csv_file = _csv_file
	_update_fn = _fn
	_output_dir = _output_folder
	# preprocess parameters
	_image_csv_file = _image_csv_file.replace("/", "\\")
	_output_dir = _output_dir.replace("/", "\\") + "\\"
	# download data
	pics_list = get_pandas_column(_image_csv_file, "images_links")
	image_remain = len(pics_list)
	_update_fn(_str="Downloading Image")
	for indx, pic in enumerate(pics_list):
		# status update call

		print(f"Downloading image.. Remaining {image_remain}")
		if "," in pic:
			tmp_pics_list = pic.split(',')
			for t in tmp_pics_list:
				download(t, _output_dir)
		else:
			download(pic, _output_dir)
		image_remain -= 1