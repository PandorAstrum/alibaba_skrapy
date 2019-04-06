# Scrapy Crawler for Alibaba
> A modifiable crawler for alibaba website to crawl and scrap product data

[![Python Version][python-image]][python-url]
[![Scrapy Version][scrapy-image]][scrapy-url]

This Repo is using various technique to scrap data from alibaba and
download product images. Also it outputs csv file from where it can be
converted to proper xml for uploading into any website via plugins or
another means.


## Installation & Setup
NOTE: Before anything, you should have Python 3 installed (preferable 3.6)

Download:
- [PYTHON](https://www.python.org/)
- [VS CODE](https://code.visualstudio.com/) for code editing but can be used any text editor like NOTEPAD


 Open up a command line tools and type:


Linux (terminal or bash):

```bash
git clone https://github.com/PandorAstrum/alibaba_skrapy.git
pip install -r requirements.txt
```
Windows (cmd):

```CMD
git clone https://github.com/PandorAstrum/alibaba_skrapy.git
pip install -r requirements.txt
```

## Folder Structure

(project root folder)

    ├── alibaba(folder)                 # contains the scrapper
    │   ├── spiders(folder)             # spider folder
    │   │   └── alibaba_spiders.py      # the main spider
    │   │
    │   ├── exporter.py                 # custom exporter for csv and xml
    │   ├── items.py                    # items to scrap
    │   ├── middlewares.py              # middlewares for the scrapper
    │   ├── pipelines.py                # pre processing stage
    │   └── settings.py                 # core settings fro the spider
    │
    ├── downlaod_image.py               # contains logic for downloading image
    ├── parameters.py                   # tweakable exposed parameter for the spider
    └── run.py                          # main file to run (runs the spider)

## Example Usage
- on the cmd or bash cd to folder where this repo is downloaded and extracted
- then type:
```
python run.py
```
It will start running the scrapper and upon finish you can check the root project folder for the output file

- to download images type:
```
python download_image.py
```
## Tweak
* in the parameters.py

**URLS**
```cs
This is a list of urls that the spider will scrap from alibaba
```
Change it according to your needs (one or many)
<br>

**OUTPUT_FILENAME**
```cs
This is the file name that will be written along with date upon scrapping finish
```
Change the name according to your needs
<br>

**CSV_FILE_FOR_IMAGE_DOWNLOAD**
```cs
This is the file name of scrapped csv file with full path to get the
list of image links for download
```
e.g: "C:\\Users\\Username\\Desktop\\project\\scrapped_Apr_05_2019_15_41_32.csv"
NOTE: dont forget the double slash to escape characters in python
<br>

## Release History

* 1.0
    * simple scrapper along with image downloader

## Meta

Ashiquzzaman Khan – [@dreadlordn](https://twitter.com/dreadlordn)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/PandorAstrum/alibaba_skrapy](https://github.com/PandorAstrum/alibaba_skrapy)

## Contributing

1. Fork it (<https://github.com/PandorAstrum/alibaba_skrapy>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.6-yellowgreen.svg?style=flat-square
[python-url]: https://www.python.org/

[scrapy-image]: https://img.shields.io/badge/scrapy-1.6-orange.svg?style=flat-square
[scrapy-url]: https://scrapy.org/

[travis-image]: https://travis-ci.org/PandorAstrum/_vault.svg?branch=master
[travis-url]: https://travis-ci.org/PandorAstrum/_vault

[appveyor-image]: https://ci.appveyor.com/api/projects/status/8dxrtild5jew79pq?svg=true
[appveyor-url]: https://ci.appveyor.com/project/PandorAstrum/vault

[ReadTheDoc]: https://github.com/yourname/yourproject/wiki

<!-- Header Pictures and Other media-->
[header-pic]: header.png
