# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Description of this file here"
"""
import pandas as pd
import requests
from parameters import CSV_FILE_FOR_IMAGE_DOWNLOAD

# read csv file Image links
#


def get_pandas_column(_filepath, _column_name, csv=True):
    if csv:
        df = pd.read_csv(_filepath)
    else:
        df = pd.read_excel(_filepath)
    return df[_column_name]


def download(url):
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)


pics_list = get_pandas_column(CSV_FILE_FOR_IMAGE_DOWNLOAD, "images_links")
image_remain = len(pics_list)
for p in pics_list:
    print(f"Downloading image.. Remaining {image_remain}")
    if "," in p:
        tmp_pics_list = p.split(',')
        for t in tmp_pics_list:
            download(t)
    else:
        download(p)
    image_remain -= 1


# url = 'http://google.com/favicon.ico'
#
